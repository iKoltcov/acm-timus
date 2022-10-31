using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Hosting;
using Microsoft.AspNetCore.Http;
// using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;

namespace H
{
    public class Program
    {
        public static void Main(string[] args)
        {
            CreateHostBuilder(args)
                .ConfigureWebHost(builder =>
                {
                    builder.UseUrls("http://localhost:7777");
                })
                .Build()
                .Run();
        }

        public static IHostBuilder CreateHostBuilder(string[] args) =>
            Host.CreateDefaultBuilder(args)
                .ConfigureWebHostDefaults(webBuilder => { webBuilder.UseStartup<Startup>(); });
    }

    public class Startup
    {
        public void ConfigureServices(IServiceCollection services)
        {
            services.AddControllers();
        }

        public void Configure(IApplicationBuilder app, IWebHostEnvironment env)
        {
            app.UseRouting();
            app.UseEndpoints(endpoints =>
            {
                endpoints.MapDefaultControllerRoute();
            });
        }
    }

    [Controller]
    [Route("[controller]")]
    public class PingController : Controller
    {
        [HttpGet]
        public async Task<IActionResult> Ping()
        {
            return await Task.FromResult<IActionResult>(Ok());
        }
    }
    
    [Controller]
    [Route("[controller]")]
    public class ShutdownController : Controller
    {
        [HttpGet]
        public async Task<IActionResult> Ping()
        {
            Environment.Exit(0);
            return await Task.FromResult<IActionResult>(Ok());
        }
    }

    [Controller]
    [Route("[controller]")]
    public class ValidatePhoneNumberController : Controller
    {
        [HttpGet]
        public async Task<IActionResult> Get([FromQuery(Name="phone_number")] string phoneNumber)
        {
            if (phoneNumber == null)
            {
                return await Task.FromResult<IActionResult>(BadRequest());
            }

            var normalized = phoneNumber
                .Replace(" ", string.Empty)
                .Replace("(", string.Empty)
                .Replace(")", string.Empty)
                .Replace("-", string.Empty);

            if (normalized.StartsWith("8"))
            {
                normalized = "+7" + normalized.Substring(1);
            }

            var code = normalized.Substring(2, 3);
            var availableCode = new[] { "982", "986", "912", "934" };
            
            if (normalized.Length != 12 || availableCode.All(x => x != code))
            {
                return await Task.FromResult<IActionResult>(
                    Ok(
                        new ErrorResponse()
                        {
                            Status = false,
                        }
                    )
                );
            }

            normalized = 
                normalized.Substring(0, 2) + "-" +
                normalized.Substring(2, 3) + "-" +
                normalized.Substring(5, 3) + "-" +
                normalized.Substring(8);

            return await Task.FromResult<IActionResult>(
                Ok(
                    new SuccessResponse()
                    {
                        Status = true,
                        Normalized = normalized,
                    }
                )
            );
        }
    }

    class SuccessResponse
    {
        public string Normalized { get; set; }

        public bool Status { get; set; }
    }

    class ErrorResponse
    {
        public bool Status { get; set; }
    }
}
# How to run locally
```bash
docker pull oscarfonts/h2
docker run -p 1521:1521 -p 81:81 -v ${PWD}/data:/opt/h2-data -e H2_OPTIONS=-ifNotExists --name=MyH2Instance oscarfonts/h2
```

# Create table:
```sql
CREATE TABLE tmp (ID INT NOT NULL)
```

# Add test data:
```sql
INSERT INTO tmp(id)
VALUES (1);
INSERT INTO tmp(id)
VALUES (1);
INSERT INTO tmp(id)
VALUES (2);
INSERT INTO tmp(id)
VALUES (3);
INSERT INTO tmp(id)
VALUES (4);
INSERT INTO tmp(id)
VALUES (5);
INSERT INTO tmp(id)
VALUES (5);
```

# And answer is:
```sql
SELECT COUNT(DISTINCT id) AS "res" 
FROM tmp;
```

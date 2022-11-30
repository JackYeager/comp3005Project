-- SQL statments as they appear in the python file

INSERT INTO "Book" ("ISBN", "Title", "Price", "Stock", "Total Sales") VALUES (%s, %s, %s, %s, %s) 
INSERT INTO "Authors" ("ISBN", "Author Name") VALUES (%s, %s)
INSERT INTO "Genre" ("ISBN", "Genre") VALUES (%s, %s)
INSERT INTO "Publisher" ("Publisher Email", "Name", "Address", "Phone Number", "Banking") VALUES (%s, %s, %s, %s, %s)
INSERT INTO "Publishes" ("ISBN", "Sales Percentage", "Publisher Email") VALUES (%s, %s, %s)
INSERT INTO "User" ("Email", "Name", "Phone Number", "Shipping Info", "Billing Info") VALUES (%s, %s, %s, %s, %s)
INSERT INTO "Orders" ("Contact Email", "Order Number", "Shipping", "Progress") VALUES (%s, %s, %s, %s)
INSERT INTO "Items" ("Order Number", "ISBN") VALUES (%s, %s)

SELECT * FROM "Book" ORDER BY "ISBN"
SELECT * FROM "Authors"
SELECT * FROM "Publisher"
SELECT * FROM "User"
SELECT * FROM "Orders"
SELECT * FROM "Publishes"
SELECT * FROM "Items"
SELECT * FROM "Genre"

SELECT "ISBN", "Title", "Total Sales", "Stock" FROM "Book" ORDER BY "ISBN"
SELECT "Book"."ISBN", "Title", "Authors"."Author Name", "Stock" FROM "Authors" INNER JOIN "Book" ON "Authors"."ISBN" = "Book"."ISBN"
SELECT "Book"."ISBN", "Title", "Authors"."Author Name", "Stock" FROM "Authors" INNER JOIN "Book" ON "Authors"."ISBN" = "Book"."ISBN" WHERE "Book"."Title"  = %s
SELECT "Author Name", SUM("Total Sales") AS sales FROM "Authors" INNER JOIN "Book" ON "Book"."ISBN"="Authors"."ISBN" GROUP BY "Author Name"
SELECT "Genre", SUM("Total Sales") AS sales FROM "Genre" INNER JOIN "Book" ON "Book"."ISBN"="Genre"."ISBN" GROUP BY "Genre"
SELECT "Progress" FROM "Orders" WHERE "Order Number" = %s
SELECT "Email" FROM "User" WHERE "User"."Email" = \'' + email + '\'

UPDATE "Book" SET "Stock" = "Stock" + %s WHERE "ISBN" = %s
UPDATE "Book" SET "Stock" = "Stock" - %s WHERE "ISBN" = %s
UPDATE "Book" SET "Stock" = "Stock" - 1, "Total Sales" = "Total Sales" + 1 WHERE "ISBN" = %s

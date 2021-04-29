-- STEP 1
-- DROP ALL TABLES
DROP TABLE IF EXISTS Users; 
DROP TABLE IF EXISTS DemotionQueue;
DROP TABLE IF EXISTS Subscriptions;
DROP TABLE IF EXISTS Posts;
DROP TABLE IF EXISTS Comments;
DROP TABLE IF EXISTS Reactions;
DROP TABLE IF EXISTS PostReactions;
DROP TABLE IF EXISTS Tags;
DROP TABLE IF EXISTS PostTags;
DROP TABLE IF EXISTS Categories;

-- STEP 2
-- CREATE TABLES
CREATE TABLE "Users" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "first_name" varchar,
  "last_name" varchar,
  "email" varchar,
  "bio" varchar,
  "username" varchar,
  "password" varchar,
  "profile_image_url" varchar,
  "created_on" date,
  "active" bit,
  "is_staff" bit
);

CREATE TABLE "DemotionQueue" (
  "action" varchar,
  "admin_id" INTEGER,
  "approver_one_id" INTEGER,
  FOREIGN KEY(`admin_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`approver_one_id`) REFERENCES `Users`(`id`),
  PRIMARY KEY (action, admin_id, approver_one_id)
);


CREATE TABLE "Subscriptions" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "follower_id" INTEGER,
  "author_id" INTEGER,
  "created_on" date,
  FOREIGN KEY(`follower_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`author_id`) REFERENCES `Users`(`id`)
);

CREATE TABLE "Posts" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "user_id" INTEGER,
  "category_id" INTEGER,
  "title" varchar,
  "publication_date" date,
  "image_url" varchar,
  "content" varchar,
  "approved" bit
);

CREATE TABLE "Comments" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "post_id" INTEGER,
  "author_id" INTEGER,
  "content" varchar,
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`),
  FOREIGN KEY(`author_id`) REFERENCES `Users`(`id`)
);

CREATE TABLE "Reactions" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" varchar,
  "image_url" varchar
);

CREATE TABLE "PostReactions" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "user_id" INTEGER,
  "reaction_id" INTEGER,
  "post_id" INTEGER,
  FOREIGN KEY(`user_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`reaction_id`) REFERENCES `Reactions`(`id`),
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`)
);

CREATE TABLE "Tags" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" varchar
);

CREATE TABLE "PostTags" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "post_id" INTEGER,
  "tag_id" INTEGER,
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`),
  FOREIGN KEY(`tag_id`) REFERENCES `Tags`(`id`)
);

CREATE TABLE "Categories" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" varchar
);

-- STEP 3
-- POPULATE TABLES

INSERT INTO Users VALUES (null, "Phineas", "Smith","108@summer.com", "What do you want to do taday Ferb?", "SummerRocks", "Perry", "N/A", "2020/25/04", 1,  0),
                         (null, "Ferb", "Smith","109@summer.com", "Where's Perry", "SummerRoxxx", "Phineas", "N/A", "2020/25/04", 0,  0),
                         (null, "Perry", "Smith","seceret@summer.com", "Doofenshmirtz sucks!", "SummerRawks", "Agent", "N/A", "2020/25/04", 1,  0);

INSERT INTO Subscriptions ('follower_id', 'author_id', 'created_on')
VALUES  (2, 3, '2021-04-26'),
        (1, 2, '2021-04-23'),
        (3, 1, '2021-04-22');

INSERT INTO Posts
VALUES (null, 1, 1, "First Launch!", "2021-04-24", "https://images.unsplash.com/photo-1518364538800-6bae3c2ea0f2?ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8bGF1bmNofGVufDB8fDB8fA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=900&q=60",
"This is all just so exciting - My first ever post!", 1 ),
(null, 1, 1, "Second post", "2021-04-25", "https://images.unsplash.com/photo-1471560090527-d1af5e4e6eb6?ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8Y2hpbGx8ZW58MHx8MHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=900&q=60",
"This seems pretty cool I guess", 1 ),
(null, 1, 1, "Final post", "2021-04-26", "https://images.unsplash.com/photo-1595521488367-9b130f86bbe3?ixid=MnwxMjA3fDB8MHxzZWFyY2h8NHx8YnllfGVufDB8fDB8fA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=900&q=60",
"This website seems like it was built by students. I'm out.", 1 ),
(null, 2, 1, "OMG Hi Guys!", "2021-04-26", "https://images.unsplash.com/photo-1613279060105-b851f33ca66b?ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8aGl8ZW58MHx8MHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=900&q=60",
"I found this picture of a smoothie and I thought y'all should see it.", 1 ),
(null, 2, 1, "Road trip!", "2021-04-26", "https://images.unsplash.com/photo-1591068594901-26711816369a?ixid=MnwxMjA3fDB8MHxzZWFyY2h8NHx8aGl8ZW58MHx8MHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=900&q=60",
"I'm moving to another state and leaving my old life behind!", 1 ),
(null, 3, 1, "Is this twitter?", "2021-04-26", "https://images.unsplash.com/photo-1572860116010-a61037d10c2d?ixid=MnwxMjA3fDB8MHxzZWFyY2h8N3x8aGl8ZW58MHx8MHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=900&q=60",
"This is not twitter, is it...", 1 );

INSERT INTO Comments
(post_id, author_id, content)
VALUES
(1,1,"Cool story bro."),
(1,2,"Ok boomer."),
(1,3,"Oh yeah right."),
(2,2,"Deeeep."),
(2,3,"2 stars. Would not read again."),
(3,1,"Zzzzz."),
(3,3,"Bee boo boo bee boo.");

INSERT INTO Reactions ('label', 'image_url') VALUES ('happy', 'https://pngtree.com/so/happy');

INSERT INTO Tags ('label')
VALUES  ('JavaScript'),
        ('Python'),
        ('Django'),
        ('Computers');

INSERT INTO PostTags
VALUES  (null,1,1),
        (null,1,2),
        (null,1,3),
        (null,2,4),
        (null,2,5),
        (null,2,1),
        (null,3,4),
        (null,3,2),
        (null,3,3);

INSERT INTO Categories ('label')
VALUES  ('Snakes'),
        ('Butts'),
        ('Cool People'),
        ('Baloons'),
        ('Parades'),
        ('Whales'),
        ('Electricity');

-- Step 4
-- TEST THAT APP BABY
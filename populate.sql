-- Add 3 posts for user 1

INSERT INTO "Posts"
VALUES (null, 1, 1, "First Launch!", "2021-04-24", "https://images.unsplash.com/photo-1518364538800-6bae3c2ea0f2?ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8bGF1bmNofGVufDB8fDB8fA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=900&q=60",
"This is all just so exciting - My first ever post!", 1 ),
(null, 1, 1, "Second post", "2021-04-25", "https://images.unsplash.com/photo-1471560090527-d1af5e4e6eb6?ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8Y2hpbGx8ZW58MHx8MHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=900&q=60",
"This seems pretty cool I guess", 1 ),
(null, 1, 1, "Final post", "2021-04-26", "https://images.unsplash.com/photo-1595521488367-9b130f86bbe3?ixid=MnwxMjA3fDB8MHxzZWFyY2h8NHx8YnllfGVufDB8fDB8fA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=900&q=60",
"This website seems like it was built by students. I'm out.", 1 )

SELECT * FROM POSTS


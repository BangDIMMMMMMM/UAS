SELECT 
    Users.Username AS "User Name",
    Games.Game_Name AS "Game Name",
    Transactions.Transaction_Date AS "Transaction Date",
    Transactions.Amount AS "Transaction Amount"
FROM 
    Transactions
JOIN 
    Users ON Transactions.User_ID = Users.User_ID
JOIN 
    Games ON Transactions.Game_ID = Games.Game_ID
WHERE 
    Transactions.Amount = (
        SELECT 
            MAX(Amount)
        FROM 
            Transactions
    );

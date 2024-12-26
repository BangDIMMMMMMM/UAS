DELIMITER $$

CREATE PROCEDURE AddTransaction(
    IN p_User_ID INT,
    IN p_Game_ID INT,
    IN p_Transaction_Date DATE,
    IN p_Amount DECIMAL(10, 2)
)
BEGIN
    INSERT INTO Transactions (User_ID, Game_ID, Transaction_Date, Amount)
    VALUES (p_User_ID, p_Game_ID, p_Transaction_Date, p_Amount);
END $$

DELIMITER ;

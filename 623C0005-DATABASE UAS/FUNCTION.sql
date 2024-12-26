DELIMITER $$

CREATE FUNCTION GetUserTransactionTotal(p_User_ID INT) 
RETURNS DECIMAL(10, 2)
DETERMINISTIC
BEGIN
    DECLARE total_amount DECIMAL(10, 2);
    SELECT SUM(Amount) INTO total_amount
    FROM Transactions
    WHERE User_ID = p_User_ID;
    RETURN total_amount;
END $$

DELIMITER ;

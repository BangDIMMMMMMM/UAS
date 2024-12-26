CREATE TABLE Games (
    Game_ID INT AUTO_INCREMENT PRIMARY KEY,
    Game_Name VARCHAR(100) NOT NULL,
    Genre_ID INT,
    FOREIGN KEY (Genre_ID) REFERENCES Genres(Genre_ID)
);

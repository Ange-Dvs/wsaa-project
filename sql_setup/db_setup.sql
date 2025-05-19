CREATE TABLE users (
    userID INT AUTO_INCREMENT PRIMARY KEY,
    firstName VARCHAR(255),
    lastName VARCHAR(255),
    age INT,
    goal VARCHAR(255)
);

CREATE TABLE workouts (
    workoutID INT AUTO_INCREMENT PRIMARY KEY,
    workout_date DATE,
    userID INT,
    sessionType VARCHAR(255),
    location VARCHAR(255),
    durationMinutes INT,
    difficulty VARCHAR(50),
    rating INT CHECK (rating BETWEEN 1 AND 5),
    FOREIGN KEY (userID) REFERENCES users(userID) ON DELETE CASCADE
);

CREATE TABLE weight_management (
    id INT AUTO_INCREMENT PRIMARY KEY,
    userID INT,
    currentWeightLogDate DATE,
    currentBodyWeight DECIMAL(5,2),
    targetBodyWeight DECIMAL(5,2),
    startingBodyWeight DECIMAL(5,2),
    FOREIGN KEY (userID) REFERENCES users(userID) ON DELETE CASCADE
);

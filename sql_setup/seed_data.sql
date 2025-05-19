-- 5 users for the users table
INSERT INTO users (firstName, lastName, age, goal) VALUES
('Emma', 'Ryan', 27, 'Lose Weight'),
('John', 'Murphy', 34, 'Build Muscle'),
('Sophia', 'Walsh', 29, 'Improve Endurance'),
('Liam', 'O''Brien', 42, 'Stay Active'),
('Ava', 'Kelly', 31, 'Tone');

-- 30 dummy workouts for the workouts table
-- The below is assuming the users are the first 5 users entered into the table. If this is not the case the value for the UserID will need to be altered before trying the insert command.
INSERT INTO workouts (workout_date, userID, sessionType, location, durationMinutes, difficulty, rating) VALUES
('2025-04-08', 5, 'HIIT', 'Home', 74, 'Easy', 4),
('2025-05-10', 5, 'HIIT', 'Studio B', 87, 'Medium', 2),
('2025-04-21', 3, 'Cardio', 'Gym A', 48, 'Easy', 4),
('2025-04-16', 4, 'Cardio', 'Gym A', 77, 'Easy', 1),
('2025-03-02', 4, 'Strength Training', 'Gym B', 84, 'Hard', 3),
('2025-05-16', 2, 'Strength Training', 'Home', 64, 'Medium', 5),
('2025-03-03', 3, 'Yoga', 'Gym B', 61, 'Hard', 3),
('2025-03-23', 3, 'Yoga', 'Gym B', 57, 'Medium', 2),
('2025-03-31', 5, 'Strength Training', 'Park', 87, 'Hard', 3),
('2025-03-10', 4, 'Strength Training', 'Gym A', 81, 'Medium', 4),
('2025-04-24', 1, 'Strength Training', 'Gym A', 35, 'Hard', 4),
('2025-04-03', 5, 'Cardio', 'Gym A', 36, 'Easy', 3),
('2025-04-10', 2, 'Cycling', 'Studio B', 88, 'Medium', 5),
('2025-05-19', 4, 'Cycling', 'Gym A', 37, 'Medium', 1),
('2025-04-15', 4, 'HIIT', 'Studio B', 78, 'Easy', 2),
('2025-05-06', 5, 'Cardio', 'Studio B', 20, 'Hard', 1),
('2025-04-11', 4, 'Cycling', 'Park', 81, 'Easy', 1),
('2025-05-16', 3, 'Yoga', 'Gym B', 24, 'Medium', 1),
('2025-03-19', 4, 'HIIT', 'Gym B', 88, 'Medium', 4),
('2025-04-30', 4, 'Strength Training', 'Studio B', 50, 'Medium', 1),
('2025-05-16', 1, 'Strength Training', 'Park', 51, 'Hard', 3),
('2025-04-11', 4, 'HIIT', 'Park', 39, 'Hard', 3),
('2025-04-13', 5, 'Strength Training', 'Gym A', 34, 'Easy', 3),
('2025-05-13', 2, 'Strength Training', 'Gym B', 89, 'Medium', 5),
('2025-03-14', 5, 'Cardio', 'Gym B', 77, 'Easy', 3),
('2025-04-16', 3, 'Cardio', 'Park', 72, 'Medium', 2),
('2025-03-06', 4, 'HIIT', 'Studio B', 37, 'Hard', 1),
('2025-03-15', 1, 'Cardio', 'Park', 49, 'Medium', 1),
('2025-04-19', 2, 'Cycling', 'Home', 81, 'Hard', 2),
('2025-04-16', 2, 'Cardio', 'Home', 43, 'Easy', 5);

-- 20 dummy weight management records
INSERT INTO weight_management (userID, currentWeightLogDate, currentBodyWeight, targetBodyWeight, startingBodyWeight) VALUES
(1, '2025-04-27', 56.61, 54.41, 60.27),
(1, '2025-03-14', 70.24, 66.91, 71.13),
(1, '2025-04-12', 63.36, 59.75, 69.71),
(1, '2025-03-16', 71.66, 69.09, 76.79),
(2, '2025-03-28', 59.52, 58.26, 66.56),
(2, '2025-05-03', 60.92, 56.32, 63.6),
(2, '2025-05-15', 63.33, 60.15, 68.13),
(2, '2025-04-22', 86.91, 82.54, 88.81),
(3, '2025-03-23', 71.88, 67.66, 79.82),
(3, '2025-05-05', 86.33, 84.81, 86.38),
(3, '2025-04-06', 68.9, 65.19, 70.37),
(3, '2025-04-05', 74.64, 71.66, 81.4),
(4, '2025-04-14', 50.34, 48.15, 60.09),
(4, '2025-03-29', 72.43, 70.71, 79.09),
(4, '2025-04-03', 67.58, 64.92, 72.61),
(4, '2025-04-30', 67.27, 63.02, 69.9),
(5, '2025-05-13', 60.88, 56.54, 65.93),
(5, '2025-03-30', 79.2, 74.65, 81.83),
(5, '2025-03-21', 83.39, 82.06, 83.83),
(5, '2025-04-19', 55.33, 51.07, 63.91);
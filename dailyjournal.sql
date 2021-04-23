CREATE TABLE `Entries` (
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`concept`	TEXT NOT NULL,
	`entry`		TEXT NOT NULL,
	`date`	INTEGER NOT NULL,
    `mood_id` INTEGER NOT NULL,
	FOREIGN KEY(`mood_id`) REFERENCES `Moods`(`id`)
);

CREATE TABLE `Moods` (
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`label`	TEXT NOT NULL
);


INSERT INTO `Entries` VALUES (null, 'sql queries', "I'm getting the hang of sql queries", 04182021, 1);

INSERT INTO `Moods` VALUES (null, 'Happy');
INSERT INTO `Moods` VALUES (null, 'OK');
INSERT INTO `Moods` VALUES (null, 'Sad');
INSERT INTO `Moods` VALUES (null, 'Angry');


SELECT * FROM `Entries`;

SELECT * FROM `Moods`;

SELECT
            e.id,
            e.concept,
            e.entry,
            e.date,
            e.mood_id,
            m.label mood_label
        FROM Entries e
        JOIN Moods m
        WHERE e.id = 1 
        AND e.mood_id = m.id;

SELECT
            m.id,
            m.label
        FROM Moods m;
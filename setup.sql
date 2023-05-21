CREATE TABLE task (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    summary VARCHAR(128),
    description TEXT,
    is_active BOOLEAN DEFAULT 1
);

INSERT INTO task (
    summary,
    description
) VALUES (
    "Take out the trash",
    "Sort trash and then take it out to the bins on the street"
);

INSERT INTO task (
    summary,
    description
) VALUES (
    "Wash the car",
    "Take car to car wash, spray with water, dry off"
);

INSERT INTO task (
    summary,
    description
) VALUES (
    "Get groceries",
    "Make grocery list, check what's already available, go to store"
);
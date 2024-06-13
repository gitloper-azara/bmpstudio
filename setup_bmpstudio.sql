-- Create categories table with necessary constraints
CREATE TABLE categories (
    id VARCHAR(60) PRIMARY KEY,
    name VARCHAR(255) NOT NULL UNIQUE,
    description TEXT
);

-- Create the photographers table with necessary constraints
CREATE TABLE photographers (
    id VARCHAR(60) PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    bio TEXT,
    email VARCHAR(255) NOT NULL UNIQUE,
    phone VARCHAR(20)
);

-- Create the images table with necessary constraints
CREATE TABLE images (
    id VARCHAR(60) PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    url VARCHAR(255) NOT NULL,
    photographer_id VARCHAR(60),
    FOREIGN KEY (photographer_id) REFERENCES photographers(id)
);

-- Create the images_categories table for the relationship between images and their categories
CREATE TABLE images_categories (
    image_id VARCHAR(60),
    category_id VARCHAR(60),
    PRIMARY KEY (image_id, category_id),
    FOREIGN KEY (image_id) REFERENCES images(id),
    FOREIGN KEY (category_id) REFERENCES categories(id)
);

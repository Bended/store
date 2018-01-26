CREATE DATABASE store;

USE store;

CREATE TABLE category (
	category INT NOT NULL AUTO_INCREMENT,
    name VARCHAR (40) NOT NULL,
    PRIMARY KEY (category));
    
CREATE TABLE products(
	id INT NOT NULL AUTO_INCREMENT,
    category INT,
    title VARCHAR (40) NOT NULL,
    description VARCHAR (255),
    price INT NOT NULL,
    favorite INT NOT NULL DEFAULT 0,
    img_url VARCHAR(255),
    PRIMARY KEY (id),
    FOREIGN KEY (category) REFERENCES category (category)
    ON UPDATE CASCADE
    ON DELETE RESTRICT);
    
describe products;
select * from products;

INSERT INTO category values (category, 'lollipop'), 
							(category, 'gum'),
                            (category, 'chocolat'),
                            (category, 'gum');


select * from category;

INSERT INTO products VALUES (id, 2, 'Ice Breakers', 'The whole family can freshen up', 3, 0, 'https://target.scene7.com/is/image/Target/14704605?wid=1560&hei=1560&fmt=pjpeg'),
							(id, 2, 'Wrigles Juicy Fruit', 'Keep things classic with Wrigley\'s Juicy Fruit', 4, 0, 'https://target.scene7.com/is/image/Target/52681091?wid=1560&hei=1560&fmt=pjpeg'),
                            (id, 3, 'Godiva Valentine\'s', 'Delicious Godiva chocolate assortment', 10, 0, 'https://target.scene7.com/is/image/Target/52792867?wid=1560&hei=1560&fmt=pjpeg'),
                            (id, 3, 'Lindt Lindor', 'Show all the special people in your life ', 9, 0, 'https://target.scene7.com/is/image/Target/52725066?wid=1560&hei=1560&fmt=pjpeg'),
                            (id, 3, 'Lindt Lindor', 'Show all the special people in your life ', 9, 0, 'https://target.scene7.com/is/image/Target/52725066?wid=1560&hei=1560&fmt=pjpeg');
                            



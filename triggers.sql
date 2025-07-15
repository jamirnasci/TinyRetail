DELIMITER //
CREATE TRIGGER dec_estoque BEFORE INSERT ON salelist
FOR EACH ROW
BEGIN
	UPDATE product p 
    SET quantity = quantity - NEW.total_item 
    WHERE p.id = NEW.product_id;
END //

DELIMITER ;
explain analyze select coalesce(sum(inventory_item_count), 0)
    from warehouse_product_statistics
    where warehouse_id = '28fb8f4a-5a02-11ea-b26e-14dda9bea6d7'

explain analyze select i.id, i.product_id,
    p.name as product_name,
    i.warehouse_id, i.quantity, i.unit_cost,
    i.currency_uom_id,
    i.created_at, i.updated_at
    from inventory_item i 
    inner join product p
        on p.id = i.product_id
    where i.warehouse_id = '28fb8f4a-5a02-11ea-b26e-14dda9bea6d7'
    order by i.created_at desc
    limit 10 offset 0

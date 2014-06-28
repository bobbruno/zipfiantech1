select SP.Name
	from SalesPerson SP
	where exists (select 'x'
					 from Orders O
					 where O.salesperson_id = SP.ID
					 group by O.salesperson_id
					 having count(O.Number)>1)

select SP.Name
	from SalesPerson SP
	where SP.ID in (select O.salesperson_id
					   from Orders O
					   group by O.salesperson_id)
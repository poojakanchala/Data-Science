-- declare 
--     v_counter number := 4;
-- begin
--     loop
--         dbms_output.put_line(v_counter) ;
--         v_counter := v_counter + 4;
--         exit when v_counter >100;
--     end loop;
-- end;


-- begin
--     for i in 1..5 loop
--          dbms_output.put_line('iterate'||i);
--          end loop;
-- end;

-- begin
--     for i in reverse 1..5 loop
--          dbms_output.put_line('iterate'||i);
--          end loop;
-- end;


-- begin
--     for i in reverse 1..5 loop
--        if mod(i,2)=0 THEN
--           dbms_output.put_line(i);
--        end if;
--     end loop;
-- end;




-- declare
--     a number := 0;
--     b number := 1;
--     c number;
-- BEGIN
--     dbms_output.put_line(a);
--     dbms_output.put_line(b);
--     for i in 1..10 loop
--        c:=a+b ;
--        dbms_output.put_line(c);
--        a := b;
--        b := c;
--     end loop;
-- end;

    

-- BEGIN
--     for i in 1..20 loop
--        for j in 1..10 loop
--         dbms_output.put_line(i|| '*' || j || '=' || i*j);
--        end loop;
--     end loop;
-- end; 

-- select * from hr.employees where hire_date = TO_DATE('2016-02-05', 'YYYY-MM-DD');
-- select * from hr.employees where job_id = 'IT_PROG'
-- select count(*) from hr.employees where salary > 17000
-- select * from hr.employees
-- select 10*2 AS MUL, 10-5 AS SUBS FROM DUAL

-- SELECT JOB_ID,AVG(SALARY) AS AVG_SALARY FROM HR.EMPLOYEES GROUP BY JOB_ID
-- SELECT * FROM HR.EMPLOYEES
-- SELECT COUNT(DISTINCT JOB_ID) FROM HR.EMPLOYEES




-- declare 
--     i number:=1;
-- BEGIN
--     WHILE i<=5 loop
--        if i = 3 THEN
--            i := i + 1;
--            continue;
--         end if;

--         dbms_output.put_line(i);
--         i := i + 1;

--     end loop;
-- end;


create or replace function bonus_cala(salary number)
return number
is 
    bonus number;
BEGIN
    if salary > 50000 THEN
      bonus := salary*0.10;
    else
      bonus := salary*0.05;
    end if;
    return bonus;
end; 
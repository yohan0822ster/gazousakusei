
print"通常形式複数個なら「y」を。colspanなら「x」を。テーブルなら「t」を：";
$y = <ARGV>;


if($y=~/y/){

print"全個数を入力：";
$x = <ARGV>;
open OUT, "> gazou.txt";

$z=($x+1);

for ($a = 1; $z > $a; $a++) {
		if ($a < 10) {
		print OUT "|photo_center\n";
         print OUT "|I\@00$a.jpg,▲▲▲|\n\n";
	}
		if ($a >= 10) {
				print OUT "|photo_center\n";
         		print OUT "|I\@0$a.jpg,▲▲▲|\n\n";
			}
	}	


close OUT;





}elsif($y=~/x/){

print"横の個数を入力：";
$x = <ARGV>;
open OUT, "> gazou.txt";
print OUT "|photo_center\n";

if ($x==1) { 
  print OUT "|I\@001.jpg,▲▲▲|";
     }
#すばらしいunlessでシンプルに。
unless ($x == 1){
     for($a = 0; $x > $a; $a++) {
         print OUT "|I\@00$a.jpg";
        }
   print OUT "|\n|M@▲▲▲|";
      }
 
close OUT;

}elsif($y=~/t/){

print"縦の個数を入力：";
$y = <ARGV>;
 
print"横の個数を入力：";
$x =<ARGV>;
 
 
open OUT, "> table.txt";
 
  print OUT "<div><table class=\"Table1\" border=\"0\" cellPadding=\"0\" cellSpacing=\"1\" >\n";
  for ($a = 0; $y > $a; $a++) {
    print OUT "<tr>\n<th>data</th>";
    for ($b = 1; $x > $b; $b++) {
      print OUT "<td>";
      print OUT "data";
      print OUT "</td>\n";
    }
    print OUT "</tr>\n";
  }
  print OUT "</table></div>\n";
 
 
close OUT;


}else{

print OUT"end";
}





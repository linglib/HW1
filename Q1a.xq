for $x in doc("books.xml")/catalog/book
order by xs:float($x/price) descending
return $x/title

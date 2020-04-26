for $a in distinct-values(doc("books.xml")//author)
return <res>
        <name>{$a}</name>
        <count>
        {count(doc("books.xml")//book[exists(index-of(author,$a))]) }
        </count>
</res>
var a = "foo";

function grandparent() {
    var b = "bar";

    function parent() {
        function nested() {
            console.log(a);
            console.log(b);
        }
        nested();
    }
    parent();
}
grandparent();
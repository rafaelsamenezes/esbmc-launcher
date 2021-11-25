fun main() {
    var x = 0;
    var y = 1;

    while(x < 20)
    {
        x += 1;
        y += x;        
    }

    assert(y > x);
}
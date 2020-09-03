package recfun

object RecFun extends RecFunInterface {

  def main(args: Array[String]): Unit = {
    println("Pascal's Triangle")
    for (row <- 0 to 10) {
      for (col <- 0 to row)
        print(s"${pascal(col, row)} ")
      println()
    }
  }

  /**
   * Exercise 1
   */
  def pascal(c: Int, r: Int): Int = if (c == 0 || c == r) 1 else pascal(c - 1, r - 1) + pascal(c, r - 1)

  /**
   * Exercise 2
   */
  import scala.annotation.tailrec
  def balance(chars: List[Char]): Boolean = {
  	    @tailrec
  	    def recur(ip: List[Char], expect: Int): Boolean = {
  	      val tmp: Int = if (ip.head == '(') expect + 1 else if (ip.head == ')') expect - 1 else expect
  	      if (tmp < 0) false
  	      else if (ip.tail.isEmpty) tmp == 0
  	      else recur(ip.tail, tmp)
  	    }
  	  recur(chars, 0)
    }	

  /**
   * Exercise 3
   */
  def countChange(money: Int, coins: List[Int]): Int = {
    def proc(S: List[Int], m: Int, n: Int): Int = if (n == 0) 1 else if (n < 0 || (m <= 0 && n >= 1)) 0 else proc(S, m - 1, n) + proc(S, m, n - S(m - 1))
    proc(coins, coins.length, money)
  }
}

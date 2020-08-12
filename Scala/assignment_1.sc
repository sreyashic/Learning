/*
Pascal's Triangle
    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1
The numbers at the edge of the triangle are all 1, and each number inside the triangle is the sum of the two numbers above it. Write a function that computes the elements of Pascal’s triangle by means of a recursive process.
Do this exercise by implementing the pascal function which takes a column c and a row r, counting from 0 and returns the number at that spot in the triangle. For example, pascal(0,2)=1,pascal(1,2)=2 and pascal(1,3)=3.
*/
def pascal(c: Int, r: Int): Int = if (c == 0 || c == r) 1 else pascal(c - 1, r - 1) + pascal(c, r - 1)
pascal(0, 2)
pascal(1, 2)
pascal(1, 3)

/*
Parentheses Balancing
Write a recursive function which verifies the balancing of parentheses in a string
*/
import scala.annotation.tailrec
def balance(chars: List[Char]): Boolean =
  {
    @tailrec
    def recur(ip: List[Char], expect: Int): Boolean =
    {
      val tmp: Int = if (ip.head == '(') expect + 1 else if (ip.head == ')') expect - 1 else expect
      if (tmp < 0) false
      else if (ip.tail.isEmpty) tmp == 0
      else recur(ip.tail, tmp)
    }
    recur(chars, 0)
  }
balance("(if (zero? x) max (/ 1 x))".toList)
balance("I told him (that it's not (yet) done).\n(But he wasn't listening)".toList)
balance(":-)".toList)
balance("())(".toList)

/*
Counting Change
Write a recursive function that counts how many different ways you can make change for an amount, given a list of coin denominations.
Source: https://www.geeksforgeeks.org/coin-change-dp-7/#:~:text=Given%20a%20value%20N%2C%20if,%2C%7B1%2C3%7D.
*/
def countChange(money: Int, coins: List[Int]): Int =
  {
    def proc(S: List[Int], m: Int, n: Int): Int = if (n == 0) 1 else if (n < 0 || (m <= 0 && n >= 1)) 0 else proc(S, m - 1, n) + proc(S, m, n - S(m - 1))
    proc(coins, coins.length, money)
  }
countChange(4,List(1,2))
countChange(300,List(5,10,20,50,100,200,500))
countChange(301,List(5,10,20,50,100,200,500))
countChange(300,List(500,5,50,100,20,200,10))

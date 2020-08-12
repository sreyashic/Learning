def sum(xs: List[Int]): Int = if (xs.isEmpty) 0 else xs.head + sum(xs.tail)

def max(xs: List[Int]): Int =
  {
    if (xs.isEmpty) throw new java.util.NoSuchElementException
    else
    {
      val tail_max: Int = if (xs.tail.isEmpty) 0 else max(xs.tail)
      if (xs.head > tail_max) xs.head else tail_max
    }
  }

sum(List(1,2,3))
sum(List())

max(List(2,3,1))
max(List())

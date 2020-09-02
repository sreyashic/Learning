import scala.annotation.tailrec

/*
Purely Functional Sets.
We represent a set by its characteristic function, i.e., its `contains` predicate.
The bounds for iterating over the set are +/- 1000.
*/
type FunSet = Int => Boolean
val bound = 1000

def contains(s: FunSet, elem: Int): Boolean = s(elem)
contains(x => x > 0, 4)
contains(x => x > 0, -4)

// Prints the contents of a set.
def toStr(s: FunSet): String = {
  val xs = for (i <- -bound to bound if contains(s, i)) yield i
  xs.mkString("{", ",", "}")
}

// 1. Returns the set of the one given element.
def singletonSet(elem: Int): FunSet = x => x == elem
val s1 = singletonSet(1)
val s2 = singletonSet(2)
val s3 = singletonSet(3)
println(toStr(s1))

// 2. Returns the union of the two given sets.
def union(s: FunSet, t: FunSet): FunSet = x => contains(s, x) | contains(t, x)
val u = union(union(s1, s2), s3)
println(toStr(u))

// 3. Returns the intersection of the two given sets.
def intersect(s: FunSet, t: FunSet): FunSet = x => contains(s, x) & contains(t, x)
println(toStr(intersect(u, s1)))

// 4. Returns the difference of the two given sets (the set of all elements of `s` that are not in `t`).
def diff(s: FunSet, t: FunSet): FunSet = x => contains(s, x) & (! contains(t, x))
println(toStr(diff(u, s1)))

// 5. Returns the subset of `s` for which `p` holds.
def filter(s: FunSet, p: Int => Boolean): FunSet = x => contains(s, x) & p(x)
println(toStr(filter(u, x => x > 1)))

// 6. Returns whether all bounded integers within `s` satisfy `p`.
def forall(s: FunSet, p: Int => Boolean): Boolean = {
  @tailrec
  def iter(a: Int): Boolean = {
    if (a > bound) true
    else if (contains(s, a) & (!p(a))) false
    else iter(a + 1)
  }
  iter(-1 * bound)
}
println(forall(u, x => x > 0))
println(forall(u, x => x > 1))

// 7. Returns whether there exists a bounded integer within `s` that satisfies `p`.
def exists(s: FunSet, p: Int => Boolean): Boolean = {
  @tailrec
  def iter(a: Int): Boolean = {
    if (a > bound) false
    else if (contains(s, a) & p(a)) true
    else iter(a + 1)
  }
  iter(-1 * bound)
}
println(exists(u, x => x > 2))
println(exists(u, x => x > 3))

// 8. Returns a set transformed by applying `f` to each element of `s`.
def map(s: FunSet, f: Int => Int): FunSet = {
  val tmp = for (i <- -bound to bound if contains(s, i)) yield f(i)
  x => tmp.contains(x)
}
println(toStr(map(u, x => x * x * x)))

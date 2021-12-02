import unittest
from LinkedList import MyLinkedStack, MyLinkedQueue 

class TestDataStructures(unittest.TestCase):

    testList = range(1,10)

    def test_stack_pop_push(self):
        stack = MyLinkedStack()
        self.assertEqual(stack.pop(), None, "ERROR: emty stack should return none")
        for i in self.testList:
            stack.push(i)
        for i in reversed(self.testList):
            popped = stack.pop()
            self.assertEqual(i, popped, f"ERROR, expected {i} but recieved {popped}")

    def test_queue_offer_poll(self):
        queue = MyLinkedQueue()
        self.assertEqual(queue.poll(), None, "ERROR: emty queue should poll none")
        testSize = 0
        for i in self.testList:
            queue.offer(i)
            testSize += 1
            self.assertEqual(testSize, queue.size, "Size is wrong")
        for i in self.testList:
            peek = queue.peek()
            polled = queue.poll()
            self.assertEqual(peek, polled, "Poll should return what was just peeked")
            self.assertEqual(i, polled, "Poll should return in the same order that we offered")

    def test_generic(self):
        bacon = set()
        bacon.add(1)
        bacon.add("dsfkjfkdf")
        mumrik = [1, 2]
        mumrik.append("dfdsfdlf")
        # Man kan fippla med generiska typer i python men det är mer standard att bara acceptera allmännare typer
        queue = MyLinkedQueue()
        queue.offer(1)
        queue.offer("testingGeneric")
        self.assertEqual(queue.poll(), 1)
        self.assertEqual(queue.poll(), "testingGeneric")

    def testing_comprehension_and_lambda(self):
        test_list = [1,2,3]
        new_list = [n + 1 for n in test_list]
        self.assertEqual(new_list, [2,3,4])
        test_dict = dict()
        test_dict[1] = "One"
        test_dict[2] = "Two"
        test_dict[3] = "Three"
        new_dict = {k:v + "Gurka" for (k, v) in test_dict.items()} #Note: k:v gives a new key value pair
        get_back_dict = {k:v.replace('Gurka','') for (k, v) in new_dict.items()} #Note: k:v gives a new key value pair
        self.assertEqual(test_dict, get_back_dict)
        
        hej = lambda x: x + 2
        self.assertEqual(3 + 2, hej(3))

if __name__ == '__main__':
    unittest.main()
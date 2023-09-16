#include <iostream>
#include "LinkedList.h"

// struct MyListNode
// {
//     /* data */
// };


void test_push_back() {
    MyLinkedList<int> list;

    list.push_back(1);
    list.push_back(2);
    list.push_back(3);

    std::cout << "Test push_back: ";
    std::cout << list._index(0)->data << ", ";
    std::cout << list._index(1)->data << ", ";
    std::cout << list._index(2)->data << std::endl;
}

void test_memory_management() {
    {
        MyLinkedList<int> list;
        for (int i = 0; i < 1000; ++i) {
            list.push_back(i);
        }
    }   

    std::cout << "Test memory management: Pushed and automatically deleted 1000 nodes." << std::endl;
}

void test_find() {
    MyLinkedList<int> list;
    list.push_back(5);
    list.push_back(10);
    list.push_back(15);

    int findVal = 10;
    auto & node = list.find(findVal);

    std::cout << "Test find: ";
    if (node && node->data == findVal) {
        std::cout << "Value " << findVal << " found." << std::endl;
    } else {
        std::cout << "Value " << findVal << " not found." << std::endl;
    }
}

void test_operator_index() {
    MyLinkedList<int> list;
    list.push_back(7);
    list.push_back(8);
    list.push_back(9);

    std::cout << "Test operator[]: ";
    std::cout << list[0] << ", ";
    std::cout << list[1] << ", ";
    std::cout << list[2] << std::endl;
}


void test_remove() {
    MyLinkedList<int> list;

    list.push_back(1);
    list.push_back(2);
    list.push_back(3);

    auto & node = list.find(1);
    int removedValue = list.remove(node);

    std::cout << "Test remove: Removed value = " << removedValue << std::endl;
    std::cout << "Remaining list: ";
    std::cout << list._index(0)->data << ", ";
    std::cout << list._index(1)->data << std::endl;
}


int main() {
    test_push_back();
    test_memory_management();
    test_find();
    test_operator_index();
    test_remove();

    std::cout << "All tests completed!" << std::endl;

    return 0;
}

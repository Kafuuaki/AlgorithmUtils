#include <memory>

// chat notes
// https://chat.openai.com/share/8c21f4db-29a7-446e-9b2d-062efe63a7ef

template <typename T> 
class MyLinkedList {
public:
private:
    struct MyListNode {
        T data;
        std::shared_ptr<MyListNode> next;
        MyListNode(const T& data) : data(data), next(nullptr) {}
    };

    std::shared_ptr<MyListNode> & _index(unsigned index, std::shared_ptr<MyListNode> root) {
        if (index == 0) {
            return root;
        }
        if (!root) {
            return std::shared_ptr<MyListNode>(nullptr);
        }
        return _index(index - 1, root->next);
    }

    std::shared_ptr<MyListNode> & find(T& data, std::shared_ptr<MyListNode> & curr) {
        if (curr == nullptr) {
            return std::shared_ptr<MyListNode>(nullptr);
        }

        if (curr->data == data) {
            return curr;
        }

        return find(data, curr->next);
    }



    std::shared_ptr<MyListNode> head_;
public:
    MyLinkedList() : head_(nullptr) {}

    void push_back(const T& data) {
        auto newNode = std::make_shared<MyListNode>(data);
        if(!head_) {
            head_ = newNode;
        } else {
            auto temp = head_;
            while(temp->next) {
                temp = temp->next;
            }
            temp->next = newNode;
        }
    }

    // recursion version of index
    std::shared_ptr<MyListNode> _index(unsigned index) {
        return _index(index, head_);
    }

    // iteration version of index
    // std::shared_ptr<MyListNode> _index(unsigned index) {
    //     if (index == 0) {
    //         return head_;
    //     } 

    //     auto curr = head_;

    //     for (unsigned i = 0; i < index; i++) {
    //         if (curr != nullptr) {
    //             curr = curr->next;
    //         } else {
    //             std::cout << "index out of ranged";
    //         }
    //     }

    //     return curr;
    // }

    T & operator[] (unsigned index) {
        std::shared_ptr<MyListNode> curr = _index(index);
        return curr->data;
    }

    std::shared_ptr<MyListNode> & find(T data) {
        return find(data, head_);
    }

    // T remove(std::shared_ptr<MyListNode> & node) {
    //     if (node == nullptr) {
    //         std::cout << "nothing to remove" << std::endl;
    //         return -1;
    //     }

    //     if (head_ == node) { // Node to remove is the head.
    //         head_ = head_->next;
    //     }


    //     auto curr = node;
    //     // detleted by raii
    //     node = node->next;
    //     std::cout << "removed" << curr->data << std::endl;
    //     T data = curr->data;

    //     return data;
    // }

    T remove(std::shared_ptr<MyListNode> & node) {
        if (node == nullptr) {
            std::cout << "nothing to remove" << std::endl;
            return -1;
        }



        T data = node->data;
        node = node->next;
        std::cout << "removed " << data << std::endl;



        // The smart pointer will handle the deletion automatically when the reference count becomes zero.

        return data;
    }

// T remove(std::shared_ptr<MyListNode> node) {
//     // if (!node) {
//     //     std::cout << "nothing to remove" << std::endl;
//     //     return -1; // or throw an exception
//     // }
    
//     // // If node is the last node, handle it differently
//     // if (!node->next) {
//     //     T data = node->data;
//     //     node.reset(); // remove the last node
//     //     return data;
//     // }

//     // // Copy data from the next node
//     // T data = node->next->data;

//     // // Adjust the next pointer to skip the next node
//     // node->next = node->next->next;
    
//     // std::cout << "removed " << data << std::endl;

//     return data;
// }



};

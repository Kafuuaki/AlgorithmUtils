#include <iostream>
#include <unordered_map>
#include <memory>
#include <vector>
using namespace std;

struct Node;
struct Item;

struct Node {
    int val;
    shared_ptr<Node> next;
    weak_ptr<Item> itemPtr;
};

struct Item {
    shared_ptr<Node> hd, tl;

    ~Item() {
        cout << "deleting item" << endl;
    }
};

class ListSet {
private:
    unordered_map<int, shared_ptr<Node>> nodeAddress;
    vector<shared_ptr<Item>> items;  // Added to keep track of created sets

public:
    void makeset(int a);
    int find(int key);
    void Union(int key1, int key2);
};

void ListSet::makeset(int a) {
    auto newSet = make_shared<Item>();
    items.push_back(newSet);  // Retain ownership of the new set

    newSet->hd = make_shared<Node>();
    newSet->tl = newSet->hd;
    nodeAddress[a] = newSet->hd;
    newSet->hd->val = a;
    newSet->hd->itemPtr = newSet;
}

// int ListSet::find(int key) {
//     if (nodeAddress.find(key) == nodeAddress.end()) {
//         cout << "Error: Key not found!" << endl;
//         return -1; // indicate error
//     }
//     return nodeAddress[key]->itemPtr->hd->val;
// }

int ListSet::find(int key) {
    if (nodeAddress.find(key) == nodeAddress.end()) {
        cout << "Error: Key not found!" << endl;
        return -1; // indicate error
    }
    
    auto itemPtrShared = nodeAddress[key]->itemPtr.lock();
    if (!itemPtrShared) {
        cout << "Error: Item no longer exists!" << endl;
        return -1; 
    }
    return itemPtrShared->hd->val;
}


// void ListSet::Union(int key1, int key2) {
//     if (nodeAddress.find(key1) == nodeAddress.end() || nodeAddress.find(key2) == nodeAddress.end()) {
//         cout << "Error: One or both keys not found!" << endl;
//         return;
//     }

//     auto set1 = nodeAddress[key1]->itemPtr;
//     auto set2 = nodeAddress[key2]->itemPtr;

//     if (set1 == set2) {
//         return; // Both keys belong to the same set
//     }

//     auto cur = set2->hd;
//     while (cur) {
//         cur->itemPtr = set1;
//         // nodeAddress.erase(cur->val); // Removing nodes of set2 from the hashmap
//         cur = cur->next;
//     }
//     set1->tl->next = set2->hd;
//     set1->tl = set2->tl;
//     cout << "set1 tl: " << set1->tl->val << endl;
// }

// void ListSet::Union(int key1, int key2) {
//     if (nodeAddress.find(key1) == nodeAddress.end() || nodeAddress.find(key2) == nodeAddress.end()) {
//         cout << "Error: One or both keys not found!" << endl;
//         return;
//     }

//     auto set1Locked = nodeAddress[key1]->itemPtr.lock();
//     if (!set1Locked) {
//         cout << "Error: Set1 no longer exists!" << endl;
//         return;
//     }

//     auto set2Locked = nodeAddress[key2]->itemPtr.lock();
//     if (!set2Locked) {
//         cout << "Error: Set2 no longer exists!" << endl;
//         return;
//     }

//     if (set1Locked == set2Locked) {
//         return; // Both keys belong to the same set
//     }

//     auto cur = set2Locked->hd;
//     while (cur) {
//         cur->itemPtr = set1Locked;
//         nodeAddress[cur->val] = cur; // Update the nodeAddress map to point to the nodes of set1
//         cur = cur->next;
//     }

//     set1Locked->tl->next = set2Locked->hd;
//     set1Locked->tl = set2Locked->tl;
//     cout << "set1 tl: " << set1Locked->tl->val << endl;
// }

void ListSet::Union(int key1, int key2) {
    if (nodeAddress.find(key1) == nodeAddress.end() || nodeAddress.find(key2) == nodeAddress.end()) {
        cout << "Error: One or both keys not found!" << endl;
        return;
    }

    auto set1Locked = nodeAddress[key1]->itemPtr.lock();
    if (!set1Locked) {
        cout << "Error: Set1 no longer exists!" << endl;
        return;
    }

    auto set2Locked = nodeAddress[key2]->itemPtr.lock();
    if (!set2Locked) {
        cout << "Error: Set2 no longer exists!" << endl;
        return;
    }

    if (set1Locked == set2Locked) {
        return; // Both keys belong to the same set
    }

    auto cur = set2Locked->hd;
    while (cur) {
        cur->itemPtr = set1Locked;
        
        // The line below isn't needed since it's just setting the existing map entry to its current value.
        // nodeAddress[cur->val] = cur; 

        cur = cur->next;
    }

    set1Locked->tl->next = set2Locked->hd;
    set1Locked->tl = set2Locked->tl;

    // Clean up nodes of set2 from the nodeAddress map
    cur = set2Locked->hd;
    while (cur) {
        nodeAddress.erase(cur->val);
        cur = cur->next;
    }
    
    // At this point, all references to set2's nodes are removed and set2 itself 
    // will be automatically deleted once all shared references to it are gone.

    cout << "set1 tl: " << set1Locked->tl->val << endl;
}



int main() {
    ListSet a;
    a.makeset(13);
    std::cout << "a, 13\n";
    a.makeset(25);
    a.makeset(45);
    a.makeset(65);

    cout << "find(13): " << a.find(13) << endl;
    cout << "find(25): " << a.find(25) << endl;
    cout << "find(65): " << a.find(65) << endl;
    cout << "find(45): " << a.find(45) << endl << endl;

    a.Union(65, 45);

    cout << "find(65): " << a.find(65) << endl;
    cout << "find(45): " << a.find(45) << endl;

    cout << "Hello World!\n";

    // nodeAddress.clear();


    return 0;
}

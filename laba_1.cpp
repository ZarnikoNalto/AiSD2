#pragma once 
#ifndef DLIST_HH 
#define DLIST_HH 

#include <memory> 
#include <stdexcept> 

namespace list { 

template<class T> 
class LinkedList { 
public: 
   LinkedList() : head_(nullptr), tail_(nullptr), size_(0) {} 
   LinkedList(const LinkedList &src); 
   LinkedList(LinkedList &&src); 
   ~LinkedList() { clear(); } 

   void push_back(T value); 
   void push_front(T value); 
   void pop_back(); 
   void pop_front(); 

   void insert(T value, size_t i); 
   void remove(size_t i); 
   T &at(size_t i); 
   void set(size_t i, T value); 

   size_t get_size() { return size_; } 
   void clear(); 
   bool is_empty() { return size_ == 0; } 

   void swap(size_t first, size_t second); 
private: 
   template<class U> 
   struct Node; 

   std::shared_ptr<Node<T>> head_; 
   std::shared_ptr<Node<T>> tail_; 

   size_t size_; 
}; 


template<class T> 
template<class U> 
struct LinkedList<T>::Node { 
   Node(U value) : next(nullptr), value(value) {} 

   std::shared_ptr<Node> next; 

   U value; 
}; 


template<class T> 
LinkedList<T>::LinkedList(const LinkedList<T> &src) : size_(0) 
{ 
   std::shared_ptr<Node<T>> cur = src.head_; 
   while (cur) { 
       push_back(cur->value); 
       cur = cur->next; 
   } 
} 

template<class T> 
LinkedList<T>::LinkedList(LinkedList<T> &&src) : size_(src.size_) 
{ 
   head_.swap(src.head_); 
   tail_.swap(src.tail_); 
} 

template<class T> 
void LinkedList<T>::push_back(T value) 
{ 
   std::shared_ptr<Node<T>> node(new Node<T>(value)); 
   if (!tail_) 
       head_ = node; 
   else 
       tail_->next = node; 
   tail_ = node; 
   ++size_; 
} 

template<class T> 
void LinkedList<T>::push_front(T value) 
{ 
   std::shared_ptr<Node<T>> node(new Node<T>(value)); 
   if (!head_) 
       tail_ = node; 
   else 
       node->next = head_; 
   head_ = node; 
   ++size_; 
} 

template<class T> 
void LinkedList<T>::pop_back() 
{ 
   if (is_empty()) 
       return; 
   if (size_ == 1) { 
       head_.reset(); 
       tail_.reset(); 
   } else { 
       std::shared_ptr<Node<T>> cur = head_; 
       while (cur != tail_ && cur->next != tail_) 
           cur = cur->next; 
       tail_ = cur; 
       tail_->next.reset(); 
   } 
   --size_; 
} 

template<class T> 
void LinkedList<T>::pop_front() 
{ 
   if (is_empty()) 
       return; 
   head_ = head_->next; 
   if (!head_) 
       tail_.reset(); 
   --size_; 
} 

template<class T> 
void LinkedList<T>::insert(T value, size_t i) 
{ 
   if (i > size_) // if i == size_, node will be inserted after the last one 
       throw std::out_of_range("Index out of range."); 
   else if (i == 0) 
       return push_front(value); 
   else if (i == size_) 
       return push_back(value); 
   std::shared_ptr<Node<T>> node(new Node<T>(value)); 
   std::shared_ptr<Node<T>> tmp; 
   if (i == size_ - 1) { 
       tmp = tail_; 
   } else { 
       tmp = head_; 
       for (size_t j = 1; j != i; ++j) 
           tmp = tmp->next; 
   } 
   node->next = tmp->next; 
   tmp->next = node; 
   ++size_; 
} 

template<class T> 
void LinkedList<T>::remove(size_t i) 
{ 
   if (i >= size_) { 
       throw std::out_of_range("Index out of range."); 
   } else if (i == 0) { 
       return pop_front(); 
   } else if (i == size_ - 1) { 
       return pop_back(); 
   } 
   std::shared_ptr<Node<T>> cur = head_; 
   for (size_t j = 1; j != i; ++j) 
       cur = cur->next; 
   std::shared_ptr<Node<T>> del = cur->next; 
   cur->next = del->next; 
   del->next.reset(); 
   --size_; 
} 

template<class T> 
T &LinkedList<T>::at(size_t i) 
{ 
   if (i >= size_) { 
       throw std::out_of_range("Index out of range."); 
   } else if (i == 0) { 
       return head_->value; 
   } else if (i == size_ - 1) { 
       return tail_->value; 
   } 
   std::shared_ptr<Node<T>> tmp = head_->next; 
   for (size_t j = 1; j != i; ++j) 
       tmp = tmp->next; 
   return tmp->value; 
} 

template<class T> 
void LinkedList<T>::set(size_t i, T value) 
{ 
   if (i >= size_) { 
       throw std::out_of_range("Index out of range."); 
   } else if (i == 0) { 
       head_->value = value; 
       return; 
   } else if (i == size_ - 1) { 
       tail_->value = value; 
       return; 
   } 
   std::shared_ptr<Node<T>> tmp = head_->next; 
   for (size_t j = 1; j != i; ++j) 
       tmp = tmp->next; 
   tmp->value = value; 
} 

template<class T> 
void LinkedList<T>::clear() 
{ 
   if (is_empty()) 
       return; 
   tail_.reset(); 
   head_.reset(); 
   size_ = 0; 
} 

template<class T> 
void LinkedList<T>::swap(size_t first, size_t second) 
{ 
   if (first >= size_ || second >= size_) 
       throw std::out_of_range("Index out of range."); 
   if (first == second) 
       return; 
   if (first > second) { 
       size_t tmp = first; 
       first = second; 
       second = tmp; 
   } 
   std::shared_ptr<Node<T>> first_prev; 
   std::shared_ptr<Node<T>> first_cur; 
   std::shared_ptr<Node<T>> second_prev; 
   std::shared_ptr<Node<T>> second_cur; 

   std::shared_ptr<Node<T>> prev = nullptr; 
   std::shared_ptr<Node<T>> cur = head_; 
   for (size_t i = 0; i < size_; ++i) { 
       if (i == first) { 
           first_prev = prev; 
           first_cur = cur; 
       } else if (i == second) { 
           second_prev = prev; 
           second_cur = cur; 
       } 
       prev = cur; 
       cur = cur->next; 
   } 

   if (tail_ == second_cur) 
       tail_ = first_cur; 
   if (head_ == first_cur) 
       head_ = second_cur; 
   else 
       first_prev->next = second_cur; 
   second_prev->next = first_cur; 
   first_cur->next.swap(second_cur->next); 
} 

}       // namespace dlist 

#endif  // DLIST_HH


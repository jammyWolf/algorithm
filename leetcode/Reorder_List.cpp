#include <iostream>
using namespace std;

#include "stdlib.h"
#include "stdio.h"
struct ListNode {
     int val;
     ListNode *next;
     ListNode(int x) : val(x), next(NULL) {}
 };
class Solution {
public:
    void reorderList(ListNode *head) {
		if(head!=NULL && head->next!=NULL && head->next->next!=NULL){
			ListNode *r, *s;
			r = head->next;
			s = r->next; 
			while(s!=NULL){
				r->next = s->next;
				s->next = r;
				r = s;
			}//while
		}//if
		else return;
    }//reorderList
};
int main(){
	ListNode a(1);
	ListNode b(2);
	ListNode c(3);
	ListNode d(4);
	a->next = b;
	b->next = c;
	c->next = d;
	ListNode a	
	return 0;
}//main

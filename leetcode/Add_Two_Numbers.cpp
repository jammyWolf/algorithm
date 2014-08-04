/**
 *Definition for singly-linked list. */
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
    ListNode *addTwoNumbers(ListNode *l1, ListNode *l2) {
		ListNode *r1, *r2, *tail;
		r1 = l1;
		r2 = l2;
		int extra = 0;
		while(r1!=NULL && r2!=NULL){
			r1->val = r1->val +r2->val+extra;
			extra = r1->val/10;
			tail = r1;
			r1 = r1->next;
			r2 = r2->next;
		}//while
		while(r1!=NULL){
			r1->val = r1->val + extra;
			tail->next = r1;
			extra = r1->val/10;
			r1 = r1->next;
		}
		while(r2!=NULL){
			r2->val = r2->val + extra;
			tail->next = r2;
			extra = r2->val/10;
			r2 = r2->next;
		}
		return l1;
    }
};

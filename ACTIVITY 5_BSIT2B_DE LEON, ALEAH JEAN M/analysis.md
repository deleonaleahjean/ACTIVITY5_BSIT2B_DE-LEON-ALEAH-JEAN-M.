

\## Why we push and pop at the head in a linked-list stack



When we add or remove items at the head of a linked list, everything happens instantly — we don’t have to search through the whole list. It takes the same amount of time no matter how big the list gets, which is really efficient. If we did it at the end instead, we’d need to walk through every single item just to reach the last one, and that gets slower as the list grows. Working at the head keeps things simple and fast.



\## Why an array queue has to be circular



A normal queue that moves forward one space at a time will eventually reach the end of the array, even though there’s empty space at the start where we already removed items. A circular queue solves this by looping back around to the beginning when it hits the end, so those empty spots get used again. That way we don’t waste space or need to move everything around just to add a new item.


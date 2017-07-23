
;; a simply queue  implement  in scheme
;; the queue is intransparent to the enviroment

;; new-queue create a queue
;; (define q (make-queue))  ---> create new queue
;; (q 'show)               ---> show the queue
;; (q 'push 'item)         ---> push the item in the queue
;; (q 'pop)                ---> pop the item in the queue
;; (q 'empty )             ---> test if the queue is empty #t #f



(define (make-queue)
  (define (new-queue) (cons '() '()))
  (define (empty-q? queue)
    (if (null? (car queue))
	#t
	#f))
  (define (insert-q! queue item)
    (let ((f (car queue)) (r (cdr queue)) (new-item  (cons item '())))
      (if (empty-q? queue)
	  (begin
	    (set-car! queue new-item)
	    (set-cdr! queue new-item))
	  (begin
	    (set-cdr! r new-item)
	    (set-cdr! queue (cdr r)))
	  ))
    item
    )

  (define (output-q! queue)
    (if (empty-q? queue)
	#f
	(let ((f (car queue)) (r (cdr queue)))
	  (set-car! queue (cdr f))
	  (car f))))
  (let ((q (new-queue)))
    (define (dispatch mess . item)
      (cond ((eq? mess 'empty?) (empty-q? q))
	    ((eq? mess 'show) q)
	    ((eq? mess 'push)
	     (if (null? item)
		 q
		 (insert-q! q (car item))))
	    ((eq? mess 'pop)
	     (if (empty-q? q )
		 '()
		 (output-q! q)))))
    dispatch))












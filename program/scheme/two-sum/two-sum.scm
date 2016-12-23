(define (index-encoding p-list)
  (define counter 0)
  (map (lambda (x)
         (set! counter (+ 1 counter))
         (cons x counter)
         ) p-list))


(define (map-cons a p-list)
  (map (lambda (x) (cons a x)) p-list ))

(define (find-n-sum p-list target n)
  ;; p-list is a (value,index) pair, which encoding by index-encoding to a specific list
  ;; this function would find 'all' possiblie answer to the solution (rather than assume there is only one answer)
  ;; if no answer found, return '() empty list
  (cond
   ((= n 0) (if (= target 0)
                (cons '() '())
                '())                  )
   ((null? p-list) (if (= n 0)
                       (cond (= target 0) (cons '() '()))
                       '()))

    (else (append (map-cons (car p-list) (find-n-sum (cdr p-list)
                                                     (- target (car (car p-list))) (- n 1)))
                  (find-n-sum (cdr p-list) target n ))
    )
    ))

(define (find-n-index-pair p-list target n)
  (define e-list (index-encoding p-list))
  (find-n-sum e-list target n))



(display (map (lambda (x)  (map (lambda (y) (cdr y)) x)) (find-n-index-pair '(32 33 33 34 35) 100 3)))
(display (map (lambda (x)  (map (lambda (y) (cdr y)) x)) (find-n-index-pair '(2 7 11 15) 9 2)))

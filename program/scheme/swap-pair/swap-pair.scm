(define (swap-pair p-list)
  (if (null? (cdr p-list))
      p-list
      (cons (car (cdr p-list)) (cons (car p-list) (swap-pair (cdr (cdr p-list)))))))


(display (swap-pair '(a b c d e f g h i a)))

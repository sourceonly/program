(define (make-table)
  (let ((table '()))
    (define (look-up t key)
      (if (null? t)
	  #f
	  (let ((x (car t)) (y (cdr t)))
	    (if (eq? key (car x))
		x
		(look-up y key)))))

    (define (update! key value)
      (let ((x (look-up table key)))
	(if (not (eq? x #f))
	    (set-cdr! x value)
	    (set! table (cons (cons key value) table)))))
    (define (dispatch mess . args)
      (cond ((eq? mess 'show) table)
	    ((eq? mess 'update) (let ((key (car args)) (value (car (cdr args))))
				  (update! key value)))
	    ((eq? mess 'lookup) (let ((key (car args)))
				  (look-up table key)))
	    ((eq? mess 'assoc) (let ((key (car args)))
				 (car (cdr (look-up table key)))))
	    ))
    
    dispatch))


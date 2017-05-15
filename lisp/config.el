;;; Package configuration

(require 'package)
(setq package-archives '(("gnu" . "https://elpa.gnu.org/packages/")
                         ("marmalade" . "https://marmalade-repo.org/packages/")
                         ("melpa" . "https://melpa.org/packages/")
                         ("org" . "http://orgmode.org/elpa/")))
(package-initialize)
(unless (package-installed-p 'use-package)
  (package-install 'use-package))

(setq use-package-verbose t)
(require 'use-package)

;;; Org mode settings

;;(use-package org :ensure t)
;;(use-package htmlize :ensure t)

;;; Loading custom backend
(add-to-list 'load-path "lisp/")
(require 'pelican-html)

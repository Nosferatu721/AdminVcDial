module.exports = {
  isLoggedIn (req, res, next) {
    if (req.isAuthenticated()) {
      return next()
    } else {
      return res.redirect('/login')
    }
  },
  isNotLoggedIn (req, res, next) {
    if (!req.isAuthenticated()) {
      return next()
    } else {
      return res.redirect('/profile')
    }
  },
  error404 (req, res) {
    res.status(404).render('auth/err404', { err404: true, title: 'Error 404' })
  }
}

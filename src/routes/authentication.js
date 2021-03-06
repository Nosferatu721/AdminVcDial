const router = require('express').Router()
const passport = require('passport')
const { isNotLoggedIn } = require('../lib/auth')

router.get('/registro', isNotLoggedIn, (req, res) => {
  res.render('auth/registro', { title: 'Registro' })
})

router.post('/registro', (req, res) => {
  res.send('Recivido')
})

router.get('/login', isNotLoggedIn, (req, res) => {
  res.render('auth/login', { title: 'CRM COS Login' })
})

router.post('/login', (req, res, next) => {
  passport.authenticate('local.login', {
    successRedirect: '/profile',
    failureRedirect: '/login',
    failureFlash: true
  })(req, res, next)
})

router.get('/logout', (req, res) => {
  req.logOut()
  res.redirect('/login')
})

module.exports = router

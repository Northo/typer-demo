import { defineAppSetup } from '@slidev/types'
import VueTermynalPlugin from "@lehoczky/vue-termynal"


export default defineAppSetup(({ app, router }) => {
  // Vue App
  app.use(VueTermynalPlugin)
})

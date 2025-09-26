import VueRouter from 'vue-router'
//引入组件
import Index from '../pages'
import Home from '../pages/home/home'
import Login from '../pages/login/login'
import Register from '../pages/register/register'
import Center from '../pages/center/center'
import Messages from '../pages/messages/list'
import ExamPaper from '../pages/exam/examPaper'
import Exam from '../pages/exam/exam'
import ExamList from '../pages/exam/examList'
import ExamRecord from '../pages/exam/examRecord'
import Storeup from '../pages/storeup/list'
import News from '../pages/news/news-list'
import NewsDetail from '../pages/news/news-detail'
import payList from '../pages/pay'

import xueshengList from '../pages/xuesheng/list'
import xueshengDetail from '../pages/xuesheng/detail'
import xueshengAdd from '../pages/xuesheng/add'
import xinliyishengList from '../pages/xinliyisheng/list'
import xinliyishengDetail from '../pages/xinliyisheng/detail'
import xinliyishengAdd from '../pages/xinliyisheng/add'
import xinlijiankangxuexiList from '../pages/xinlijiankangxuexi/list'
import xinlijiankangxuexiDetail from '../pages/xinlijiankangxuexi/detail'
import xinlijiankangxuexiAdd from '../pages/xinlijiankangxuexi/add'
import fudaoyuyueList from '../pages/fudaoyuyue/list'
import fudaoyuyueDetail from '../pages/fudaoyuyue/detail'
import fudaoyuyueAdd from '../pages/fudaoyuyue/add'
import scoredeterminationList from '../pages/scoredetermination/list'
import scoredeterminationDetail from '../pages/scoredetermination/detail'
import scoredeterminationAdd from '../pages/scoredetermination/add'
import newstypeList from '../pages/newstype/list'
import newstypeDetail from '../pages/newstype/detail'
import newstypeAdd from '../pages/newstype/add'
import aboutusList from '../pages/aboutus/list'
import aboutusDetail from '../pages/aboutus/detail'
import aboutusAdd from '../pages/aboutus/add'
import discussxinlijiankangxuexiList from '../pages/discussxinlijiankangxuexi/list'
import discussxinlijiankangxuexiDetail from '../pages/discussxinlijiankangxuexi/detail'
import discussxinlijiankangxuexiAdd from '../pages/discussxinlijiankangxuexi/add'

const originalPush = VueRouter.prototype.push
VueRouter.prototype.push = function push(location) {
	return originalPush.call(this, location).catch(err => err)
}

//配置路由
export default new VueRouter({
	routes:[
		{
      path: '/',
      redirect: '/index/home'
    },
		{
			path: '/index',
			component: Index,
			children:[
				{
					path: 'home',
					component: Home
				},
				{
					path: 'center',
					component: Center,
				},
				{
					path: 'pay',
					component: payList,
				},
				{
					path: 'messages',
					component: Messages
				},
				{
					path: 'examPaper',
					component: ExamPaper
				},
				{
					path: 'examList',
					component:ExamList
				},
				{
					path: 'examRecord/:type',
					component:ExamRecord
				},
				{
					path: 'storeup',
					component: Storeup
				},
				{
					path: 'news',
					component: News
				},
				{
					path: 'newsDetail',
					component: NewsDetail
				},
				{
					path: 'xuesheng',
					component: xueshengList
				},
				{
					path: 'xueshengDetail',
					component: xueshengDetail
				},
				{
					path: 'xueshengAdd',
					component: xueshengAdd
				},
				{
					path: 'xinliyisheng',
					component: xinliyishengList
				},
				{
					path: 'xinliyishengDetail',
					component: xinliyishengDetail
				},
				{
					path: 'xinliyishengAdd',
					component: xinliyishengAdd
				},
				{
					path: 'xinlijiankangxuexi',
					component: xinlijiankangxuexiList
				},
				{
					path: 'xinlijiankangxuexiDetail',
					component: xinlijiankangxuexiDetail
				},
				{
					path: 'xinlijiankangxuexiAdd',
					component: xinlijiankangxuexiAdd
				},
				{
				{
					path: 'zhenshixinxiAdd',
					component: zhenshixinxiAdd
				},
				{
					path: 'fudaoyuyue',
					component: fudaoyuyueList
				},
				{
					path: 'fudaoyuyueDetail',
					component: fudaoyuyueDetail
				},
				{
					path: 'fudaoyuyueAdd',
					component: fudaoyuyueAdd
				},
				{
					path: 'scoredetermination',
					component: scoredeterminationList
				},
				{
					path: 'scoredeterminationDetail',
					component: scoredeterminationDetail
				},
				{
					path: 'scoredeterminationAdd',
					component: scoredeterminationAdd
				},
				{
					path: 'newstype',
					component: newstypeList
				},
				{
					path: 'newstypeDetail',
					component: newstypeDetail
				},
				{
					path: 'newstypeAdd',
					component: newstypeAdd
				},
				{
					path: 'aboutus',
					component: aboutusList
				},
				{
					path: 'aboutusDetail',
					component: aboutusDetail
				},
				{
					path: 'aboutusAdd',
					component: aboutusAdd
				},
				{
					path: 'discussxinlijiankangxuexi',
					component: discussxinlijiankangxuexiList
				},
				{
					path: 'discussxinlijiankangxuexiDetail',
					component: discussxinlijiankangxuexiDetail
				},
				{
					path: 'discussxinlijiankangxuexiAdd',
					component: discussxinlijiankangxuexiAdd
				},
				{
					path: 'discusszhenshixinxi',
					component: discusszhenshixinxiList
				},
				{
					path: 'discusszhenshixinxiDetail',
					component: discusszhenshixinxiDetail
				},
				{
					path: 'discusszhenshixinxiAdd',
					component: discusszhenshixinxiAdd
				},
			]
		},
		{
			path: '/login',
			component: Login
		},
		{
			path: '/register',
			component: Register
		},
		{
			path: '/exam',
			component: Exam
		}
	]
})

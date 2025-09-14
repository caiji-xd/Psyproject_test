import Vue from 'vue';
//配置路由
import VueRouter from 'vue-router'
Vue.use(VueRouter);
//1.创建组件
import Index from '@/views/index'
import Home from '@/views/home'
import Login from '@/views/login'
import NotFound from '@/views/404'
import UpdatePassword from '@/views/update-password'
import pay from '@/views/pay'
import register from '@/views/register'
import center from '@/views/center'
import adminexam from '@/views/modules/exampaperlist/exam'
	import xinliyisheng from '@/views/modules/xinliyisheng/list'
	import news from '@/views/modules/news/list'
	import aboutus from '@/views/modules/aboutus/list'
	import xinlijiankangxuexi from '@/views/modules/xinlijiankangxuexi/list'
	import xuesheng from '@/views/modules/xuesheng/list'
	import examquestion from '@/views/modules/examquestion/list'
	import discussxinlijiankangxuexi from '@/views/modules/discussxinlijiankangxuexi/list'
	import scoredetermination from '@/views/modules/scoredetermination/list'
	import discusszhenshixinxi from '@/views/modules/discusszhenshixinxi/list'
	import zhenshixinxi from '@/views/modules/zhenshixinxi/list'
	import exampaper from '@/views/modules/exampaper/list'
	import fudaoyuyue from '@/views/modules/fudaoyuyue/list'
	import messages from '@/views/modules/messages/list'
	import config from '@/views/modules/config/list'
	import examrecord from '@/views/modules/examrecord/list'
	import newstype from '@/views/modules/newstype/list'


//2.配置路由   注意：名字
export const routes = [{
	path: '/',
	name: '系统首页',
	component: Index,
	children: [{
		// 这里不设置值，是把main作为默认页面
		path: '/',
		name: '系统首页',
		component: Home,
		meta: {icon:'', title:'center', affix: true}
	}, {
		path: '/updatePassword',
		name: '修改密码',
		component: UpdatePassword,
		meta: {icon:'', title:'updatePassword'}
	}, {
		path: '/pay',
		name: '支付',
		component: pay,
		meta: {icon:'', title:'pay'}
	}, {
		path: '/center',
		name: '个人信息',
		component: center,
		meta: {icon:'', title:'center'}
	}
	,{
		path: '/xinliyisheng',
		name: '教师',
		component: xinliyisheng
	}
	,{
		path: '/news',
		name: '公告通知',
		component: news
	}
	,{
		path: '/aboutus',
		name: '关于我们',
		component: aboutus
	}
	,{
		path: '/xinlijiankangxuexi',
		name: '心理健康学习',
		component: xinlijiankangxuexi
	}
	,{
		path: '/xuesheng',
		name: '学生',
		component: xuesheng
	}
	,{
		path: '/examquestion',
		name: '试题管理',
		component: examquestion
	}
	,{
		path: '/discussxinlijiankangxuexi',
		name: '心理健康学习评论',
		component: discussxinlijiankangxuexi
	}
	,{
		path: '/scoredetermination',
		name: '测评结果分析',
		component: scoredetermination
	}
	,{
		path: '/discusszhenshixinxi',
		name: '诊室信息评论',
		component: discusszhenshixinxi
	}
	,{
		path: '/zhenshixinxi',
		name: '诊室信息',
		component: zhenshixinxi
	}
	,{
		path: '/exampaper',
		name: '心理测试管理',
		component: exampaper
	}
	,{
		path: '/fudaoyuyue',
		name: '辅导预约',
		component: fudaoyuyue
	}
	,{
		path: '/messages',
		name: '留言反馈',
		component: messages
	}
	,{
		path: '/config',
		name: '轮播图管理',
		component: config
	}
	,{
		path: '/examrecord',
		name: '心理测试记录',
		component: examrecord
	}
	,{
		path: '/newstype',
		name: '公告通知分类',
		component: newstype
	}
	]
	},
	{
		path: '/adminexam',
		name: 'adminexam',
		component: adminexam,
		meta: {icon:'', title:'adminexam'}
	},
	{
		path: '/login',
		name: 'login',
		component: Login,
		meta: {icon:'', title:'login'}
	},
	{
		path: '/register',
		name: 'register',
		component: register,
		meta: {icon:'', title:'register'}
	},
	{
		path: '*',
		component: NotFound
	}
]
//3.实例化VueRouter  注意：名字
const router = new VueRouter({
	mode: 'hash',
	/*hash模式改为history*/
	routes // （缩写）相当于 routes: routes
})
const originalPush = VueRouter.prototype.push
//修改原型对象中的push方法
VueRouter.prototype.push = function push(location) {
	return originalPush.call(this, location).catch(err => err)
}
export default router;

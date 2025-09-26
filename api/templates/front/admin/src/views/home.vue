<template>
	<div class="home-content">
		<!-- title -->
		<div id="home-title" class="home-title animate__animated">
			<div class="titles" >
				<span>欢迎使用</span>
				{{this.$project.projectName}}
			</div>
		</div>
		<div id="news-box" class="news-box animate__animated">
			<div class="news-title">
				公告通知
			</div>
			<div class="news-list">
				<div class="news-item" v-for="(item,index) in newsList" :index="index" @click="newsDetailClick(item)">
					<div class="news-text">
						{{item.title}}
					</div>
					<div class="news-time">
						{{item.addtime}}
					</div>
				</div>
			</div>
		</div>
		<el-dialog :visible.sync="newsVisible" title="公告通知" :append-to-body="true" width="60%">
			<div style="width: 100%;text-align: center;font-size: 20px;color: #000;padding: 0 0 20px;font-weight: bold;">{{newsDetail.title}}</div>
			<div style="width: 100%;">
				<div class="ql-snow ql-editor" v-html="newsDetail.content"></div>
			</div>
		</el-dialog>
		<!-- 日历 -->
		<div id="calendar" class="calendar animate__animated">
			<div class="option">
				<div class="pyear" @click="pyear"><span class="icon iconfont icon-fanhui"></span>上一年</div>
				<div class="pmonth" @click="pmonth"><span class="icon iconfont icon-fanhui"></span>上一月</div>
				<div class="date-box">
					<div class="year">{{this.year}}年</div>
					<div class="month">{{this.month}}月</div>
				</div>
				<div class="nmonth" @click="nmonth">下一月<span class="icon iconfont icon-jinru"></span></div>
				<div class="nyear" @click="nyear">下一年<span class="icon iconfont icon-jinru"></span></div>
			</div>
			<table v-if="this.weeks.length">
				<thead>
					<tr>
						<th v-for="item,index in this.heads" :key="index">{{item}}</th>
					</tr>
				</thead>
				<tbody>
					<tr v-for="week,index in this.weeks" :key="index">
						<td v-for="day,key in week.days" :key="key" :class="{other: day.isOther, festival: day.isFestival, today: day.isToday, rest: day.isRest}">
							<div class="text">
								<div class="new">{{day.day}}</div>
								<div class="old">{{day.text}}</div>
							</div>
						</td>
					</tr>
				</tbody>
			</table>
		</div>
	
		<!-- echarts -->
	</div>
</template>
<script>
import 'animate.css'
//0
import router from '@/router/router-static'
import * as echarts from 'echarts'
export default {
	data() {
		return {
			// 日历
			year: 2023,
			month: 6,
			heads: ['一', '二', '三', '四', '五', '六', '日'],
			weeks: [],
			now: Solar.fromDate(new Date()),
			newsList: [],
			newsDetail: {},
			newsVisible: false,
		};
	},
	mounted(){
		this.init();
		window.addEventListener('scroll', this.handleScroll)
		setTimeout(()=>{
			this.handleScroll()
		},100)
	},
	computed: {
		avatar(){
			return this.$storage.get('headportrait')?this.$storage.get('headportrait'):''
		},
	},
	methods:{
		handleScroll() {
			let arr = [
				{id:'home-title',css:'animate__'},
				{id:'news-box',css:'animate__'},
				{id:'calendar',css:'animate__'},
			]
			
			for (let i in arr) {
				let doc = document.getElementById(arr[i].id)
				if (doc) {
					let top = doc.offsetTop
					let win_top = window.innerHeight + window.pageYOffset
					// console.log(top,win_top)
					if (win_top > top && doc.classList.value.indexOf(arr[i].css) < 0) {
						// console.log(doc)
						doc.classList.add(arr[i].css)
					}
				}
			}
		},
		init(){
			if(this.$storage.get('Token')){
				this.$http({
					url: `${this.$storage.get('sessionTable')}/session`,
					method: "get"
				}).then(({ data }) => {
					if (data && data.code != 0) {
						router.push({ name: 'login' })
					}
				});
			}else{
				router.push({ name: 'login' })
			}
			this.$nextTick(() => {
				// --- 日历 ---
				this.year = this.now.getYear()
				this.month = this.now.getMonth()
				this.weeks = this.render(this.year, this.month);
			})
			this.getNewsList()
		},
		getNewsList(){
			let params = {
				page: 1,
				limit: 6,
				sort: 'addtime',
				order: 'desc',
			}
			this.$http({
				url: `news/list`,
				method: "get",
				params: params
			}).then(res => {
				if(res.data&&res.data.code==0){
					this.newsList = res.data.data.list
				}
			});
		},
		newsDetailClick(row){
			this.newsDetail = row
			this.newsVisible = true
		},
		// 日历
		nyear() {
			this.year = this.year + 1
			this.weeks = this.render(this.year, this.month)
		},
		pyear() {
			this.year = this.year - 1
			this.weeks = this.render(this.year, this.month)
		},
		nmonth() {
			this.month = this.month + 1
			if (this.month > 12) {
				this.month = 1
				this.year = this.year + 1
			}
			this.weeks = this.render(this.year, this.month)
		},
		pmonth() {
			this.month = this.month - 1
			if (this.month < 1) {
				this.month = 12
				this.year = this.year - 1
			}
			this.weeks = this.render(this.year, this.month)
		},
		// 日历
		render(year, month, weekStart = 1) {
			let months = SolarMonth.fromYm(year, month)
			let weeks = []
		
			months.getWeeks(weekStart).forEach(w => {
				let week = {
					index: 0,
					days: []
				}
				week.index = w.getIndexInYear()
				let days = []
				w.getDays().forEach(d => {
					days.push(this.buildDay(d, month))
				})
				week.days = days
				weeks.push(week)
			})
			return weeks
		},
		buildDay(d, month) {
			let lunar = d.getLunar()
			let day = {
				day: 0,
				text: '',
				isFestival: false,
				isToday: false,
				isOther: false,
				isHoliday: false,
				isRest: false
			}
			day.day = d.getDay()
			let text = lunar.getDayInChinese()
			if (1 === d.getDay()) {
				text = lunar.getMonthInChinese() + '月'
			}
			// let otherFestivals = d.getOtherFestivals()
			// if (otherFestivals.length > 0) {
			// 	text = otherFestivals[0]
			// 	day.isFestival = true
			// }
			// otherFestivals = lunar.getOtherFestivals()
			// if (otherFestivals.length > 0) {
			// 	text = otherFestivals[0]
			// 	day.isFestival = true
			// }
			let festivals = d.getFestivals()
			if (festivals.length > 0) {
				text = festivals[0]
				day.isFestival = true
			}
			festivals = lunar.getFestivals()
			if (festivals.length > 0) {
				text = festivals[0]
				day.isFestival = true
			}
			let jq = lunar.getJieQi()
			if (jq) {
				text = jq
				day.isFestival = true
			}
			day.text = text
			if (d.toYmd() === this.now.toYmd()) {
				day.isToday = true
			}
			if (d.getMonth() !== month) {
				day.isOther = true
			}
			let h = HolidayUtil.getHoliday(d.getYear(), d.getMonth(), d.getDay())
			if (h) {
				day.isHoliday = true
				day.isRest = !h.isWork()
			}
			return day
		},
		// 日历
	}
};
</script>
<style lang="scss" scoped>
	.home-content {
		padding: 10px 30px;
		background: url() no-repeat center top / cover,#f7f7f7;
		display: flex;
		width: 100%;
		min-height: 100vh;
		justify-content: flex-start;
		align-items: flex-start;
		flex-wrap: wrap;
		.home-title {
			border-radius: 5px;
			padding: 10px 0;
			box-shadow: 0 0px 0px rgba(0,0,0,.3);
			margin: 10px 0;
			background: none;
			display: flex;
			width: 100%;
			justify-content: center;
			align-items: center;
			transition: 0.3s;
			.titles {
				padding: 0 0 0 12px;
				color: #333;
				font-size: 26px;
				line-height: 44px;
				span {
				}
			}
		}
		.home-title:hover {
			transform: translate3d(0, 0px, 0);
			z-index: 1;
			background: rgba(255,255,255,.12);
		}
		.news-box {
			border: 0px solid #ccc;
			padding: 0;
			margin: 10px;
			display: block;
			min-height: 462px;
			transition: 0.3s;
			border-radius: 10px;
			box-shadow: 0 0px 0px rgba(0,0,0,.3);
			flex-direction: column;
			background: #fff;
			width: calc(30% - 20px);
			justify-content: center;
			align-items: center;
			order: 10;
			.news-title {
				padding: 0 10px;
				margin: 0 0 10px;
				color: #fff;
				font-weight: 500;
				font-size: 20px;
				border-color: #e6e6e6;
				line-height: 60px;
				border-radius: 10px 10px 0 0;
				background: #7841f0;
				width: 100%;
				border-width: 0 0 0px;
				border-style: solid;
				text-align: center;
			}
			.news-list {
				padding: 0 20px;
				flex-direction: column;
				display: flex;
				width: 100%;
				justify-content: space-between;
				align-items: center;
			}
			.news-item {
				border: 1px dashed #eee;
				cursor: pointer;
				padding: 10px 10px;
				display: flex;
				width: 100%;
				border-width: 0 0 1px;
				justify-content: space-between;
				align-items: center;
				.news-text {
					overflow: hidden;
					color: #000;
					white-space: nowrap;
					font-weight: 500;
					width: 100%;
					font-size: 15px;
					text-overflow: ellipsis;
				}
				.news-time {
					color: #999;
					display: none;
					font-size: 14px;
				}
			}
		}
		.news-box:hover {
			transform: translate3d(0, 0px, 0);
		}
		.calendar {
			border: 0px solid #ccc;
			border-radius: 10px;
			box-shadow: 0 0px 0px rgba(0,0,0,.1);
			margin: 10px;
			background: #eaecf3;
			width: calc(70% - 20px);
			transition: 0.3s;
			height: auth;
			order: 11;
			.option {
				border-radius: 10px 10px 0 0;
				padding: 10px 20px;
				color: #fff;
				background: #7841f0;
				display: flex;
				width: 100%;
				font-size: 16px;
				justify-content: space-between;
				flex-wrap: wrap;
				height: auto;
				.pyear {
					cursor: pointer;
					border-radius: 4px;
					padding: 0 12px;
					color: inherit;
					background: none;
					font-weight: 600;
					display: flex;
					width: auto;
					font-size: inherit;
					justify-content: center;
					align-items: center;
					height: 40px;
					.iconfont {
						margin: 0 2px;
						color: inherit;
						display: none;
						font-size: inherit;
					}
				}
				.pyear:hover {
					opacity: 0.8;
				}
				.pmonth {
					cursor: pointer;
					border-radius: 4px;
					padding: 0 12px;
					color: inherit;
					background: none;
					font-weight: 600;
					display: flex;
					width: auto;
					font-size: inherit;
					justify-content: center;
					align-items: center;
					height: 40px;
					.iconfont {
						margin: 0 2px;
						color: inherit;
						display: none;
						font-size: inherit;
					}
				}
				.pmonth:hover {
					opacity: 0.8;
				}
				.date-box {
					padding: 0 10px;
					display: flex;
					justify-content: center;
					align-items: center;
					.year {
						margin: 0 2px;
						color: inherit;
						font-size: 24px;
					}
					.month {
						margin: 0 2px;
						color: inherit;
						font-size: 24px;
					}
				}
				.nmonth {
					cursor: pointer;
					border-radius: 4px;
					padding: 0 12px;
					color: inherit;
					background: none;
					font-weight: 600;
					display: flex;
					width: auto;
					font-size: inherit;
					justify-content: center;
					align-items: center;
					height: 40px;
					.iconfont {
						margin: 0 2px;
						color: inherit;
						display: none;
						font-size: 16px;
					}
				}
				.nmonth:hover {
					opacity: 0.8;
				}
				.nyear {
					cursor: pointer;
					border-radius: 4px;
					padding: 0 12px;
					color: inherit;
					background: none;
					font-weight: 600;
					display: flex;
					width: auto;
					font-size: inherit;
					justify-content: center;
					align-items: center;
					height: 40px;
					.iconfont {
						margin: 0 2px;
						color: inherit;
						display: none;
						font-size: inherit;
					}
				}
				.nyear:hover {
					opacity: 0.8;
				}
			}
			table {
				border-radius: 0 0 10px 10px;
				padding: 0;
				background: #fff;
				width: 100%;
				heith: auto;
				thead {
					width: 100%;
					heith: auto;
					tr {
						display: flex;
						width: 100%;
						heith: auto;
						justify-content: center;
						align-items: center;
						th {
							color: #666;
							flex: 1;
							display: flex;
							font-size: 16px;
							line-height: 40px;
							justify-content: center;
							align-items: center;
						}
					}
				}
				tbody {
					width: 100%;
					heith: auto;
					tr {
						display: flex;
						width: 100%;
						heith: auto;
						justify-content: center;
						align-items: center;
						td {
							cursor: pointer;
							padding: 5px 15px 0;
							flex: 1;
							display: flex;
							height: auto;
							.text {
								border-radius: 4px;
								flex-direction: column;
								background: #fff;
								display: flex;
								width: 100%;
								justify-content: center;
								align-items: center;
								height: 100%;
							}
							.text:hover {
								background: none;
							}
							.text .new {
								color: #000;
								font-size: 20px;
								line-height: 1.4;
							}
							.text .old {
								color: #666;
								font-size: 14px;
								line-height: 1.4;
							}
						}
						td.festival {
							.text {
								border-radius: 4px;
								flex-direction: column;
								background: rgba(120, 65, 240,.1);
								display: flex;
								width: 100%;
								justify-content: center;
								align-items: center;
								height: 100%;
							}
							.text:hover {
								background: rgba(120, 65, 240,.2);
							}
							.text .new {
								color: #000;
								font-size: 24px;
								line-height: 1.4;
							}
							.text .old {
								color: #666;
								font-size: 16px;
								line-height: 1.4;
							}
						}
						td.other {
							.text {
								border-radius: 4px;
								padding: 0 0 10px;
								flex-direction: column;
								background: #fff;
								display: flex;
								width: 100%;
								justify-content: center;
								align-items: center;
								opacity: 0.3;
								height: 100%;
							}
							.text:hover {
								background: none;
							}
							.text .new {
								color: #000;
								font-size: 20px;
								line-height: 1.4;
							}
							.text .old {
								color: #666;
								font-size: 14px;
								line-height: 1.4;
							}
						}
						td.today {
							.text {
								border-radius: 4px;
								flex-direction: column;
								color: #fff;
								background: rgba(120, 65, 240,.6);
								display: flex;
								width: 100%;
								justify-content: center;
								align-items: center;
								height: 100%;
							}
							.text:hover {
								background: rgba(120, 65, 240,.5);
							}
							.text .new {
								color: inherit;
								font-size: 20px;
								line-height: 1.4;
							}
							.text .old {
								color: inherit;
								font-size: 14px;
								line-height: 1.4;
							}
						}
					}
				}
			}
		}
		.calendar:hover {
			transform: translate3d(0, 0px, 0);
			z-index: 1;
		}
	}
	
	.echarts-flag-2 {
		display: flex;
		flex-wrap: wrap;
		justify-content: space-between;
		padding: 10px 20px;
		background: rebeccapurple;
	
		&>div {
			width: 32%;
			height: 300px;
			margin: 10px 0;
			background: rgba(255,255,255,.1);
			border-radius: 8px;
			padding: 10px 20px;
		}
	}
	.animate__animated {
		animation-fill-mode: none;
	}
</style>

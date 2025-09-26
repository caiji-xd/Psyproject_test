<template>
	<div>
		<div class="breadcrumb-preview">
			<el-breadcrumb :separator="'>'">
				<el-breadcrumb-item class="item1" to="/"><a>首页</a></el-breadcrumb-item>
				<el-breadcrumb-item class="item2" v-for="(item, index) in breadcrumbItem" :key="index"><a>{{item.name}}</a></el-breadcrumb-item>
			</el-breadcrumb>
		</div>
	
		<div class="news-preview-pv">
			<el-form :inline="true" :model="formSearch" class="list-form-pv">
				<el-form-item class="search-item">
					<el-input v-model="title" placeholder="标题"></el-input>
				</el-form-item>
				<el-button class="search-btn" type="primary" @click="getNewsList(1)">
					<span class="icon iconfont icon-chakan14"></span>
					搜索
				</el-button>
			</el-form>
			
			<!-- category -->
			<div class="category-list">
				<div class="item" @click="categoryClick(0)" :class="categoryIndex == 0 ? 'active' : ''">全部</div>
				<div v-for="(item,index) in categoryList" @click="categoryClick(index+1)" :key="index" class="item" :class="categoryIndex == index+1 ? 'active' : ''">{{item.typename}}</div>
			</div>
			<div class="list12">
				<div class="list-item1" @click="toNewsDetail(newsList[0])">
					<div class="img">
						<img :src="baseUrl + newsList[0].picture" alt="">
					</div>
					<div class="infoBox">
						<div class="name">{{newsList[0].title}}</div>
						<div class="desc">{{newsList[0].introduction}}</div>
						<div class="infoCenter">
							<div class="time_item">
								<span class="icon iconfont "></span>
								<span class="label">发布时间：</span>
								<span class="text">{{newsList[0].addtime.split(' ')[0]}}</span>
							</div>
							<div class="publisher_item">
								<span class="icon iconfont "></span>
								<span class="label">发布人：</span>
								<span class="text">{{newsList[0].name}}</span>
							</div>
							<div class="like_item">
								<span class="icon iconfont "></span>
								<span class="label">点赞：</span>
								<span class="text">{{newsList[0].thumbsupnum}}</span>
							</div>
							<div class="collect_item">
								<span class="icon iconfont "></span>
								<span class="label">收藏：</span>
								<span class="text">{{newsList[0].storeupnum}}</span>
							</div>
							<div class="view_item">
								<span class="icon iconfont "></span>
								<span class="label">浏览次数：</span>
								<span class="text">{{newsList[0].clicknum}}</span>
							</div>
						</div>
						<div class="more_btn">
							<span class="text">查看更多</span>
							<span class="icon iconfont icon-gengduo1"></span>
						</div>
					</div>
				</div>
				<div class="list-body">
					<div class="list-body-left">
						<div v-if="index>0&&index<=Number(3)" v-for="(item,index) in newsList" :key="index" class="list-item" @click="toNewsDetail(item)">
							<div class="img">
								<img :src="baseUrl + item.picture" alt="">
							</div>
							<div class="name">{{item.title}}</div>
						</div>
					</div>
					<div class="list-body-right">
						<div v-if="index>Number(3)&&index<=Number(4)" v-for="(item,index) in newsList" :key="index" class="list-item" @click="toNewsDetail(item)">
							<div class="infoBox">
								<div class="name">{{item.title}}</div>
								<div class="desc">{{item.introduction}}</div>
							</div>
							<div class="time_item">
								<div class="day">{{item.addtime.split(' ')[0].split('-')[1]}}-{{item.addtime.split(' ')[0].split('-')[2]}}</div>
								<div class="year">{{item.addtime.split(' ')[0].split('-')[0]}}</div>
							</div>
						</div>
					</div>
				</div>
			</div>
		
			<el-pagination
				background
				id="pagination" class="pagination"
				:pager-count="7"
				:page-size="pageSize"
				:page-sizes="pageSizes"
				prev-text="上一页"
				next-text="下一页"
				:hide-on-single-page="false"
				:layout='["total","prev","pager","next","sizes","jumper"].join()'
				:total="total"
				@current-change="curChange"
				@prev-click="prevClick"
				@next-click="nextClick"
				></el-pagination>

			<!-- 热门信息 -->
			<div class="hot">
				<div class="hot-title">热门信息</div>
				<div class="hot-list">
					<div class="hot-item" v-for="item in hotList" :key="item.id" @click="toNewsDetail(item)">
						<img :src="baseUrl + item.picture" alt="">
						<div class="hot-name">{{ item.title }}</div>
						<div class="hot-time">{{item.addtime}}</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
	export default {
		//数据集合
		data() {
			return {
				baseUrl: this.$config.baseUrl,
				breadcrumbItem: [
				  {
					name: '公告通知'
				  }
				],
				newsList: [],
				total: 1,
				pageSize: 10,
				pageSizes: [],
				totalPage: 1,
				layouts: '',
				title: '',
				categoryIndex: 0,
				categoryList: [],
				hotList: [],
			}
		},
		created() {
			this.getCategoryList()
			this.getNewsList(1);
			this.getHotList()
		},
		//方法集合
		methods: {
			getCategoryList(){
				this.$http.get('newstype/list', {}).then(res => {
					if (res.data.code == 0) {
						this.categoryList = res.data.data.list
					}
				});
			},
			categoryClick(index) {
				this.categoryIndex = index
				this.getNewsList()
			},
			getNewsList(page) {
				let params = {page, limit: this.pageSize,sort:'addtime',order:'desc'};
				let searchWhere = {};
				if(this.title != '') searchWhere.title = '%' + this.title + '%';
				if(this.categoryIndex!=0){
					searchWhere.typename = this.categoryList[this.categoryIndex - 1].typename
				}
				this.$http.get('news/list', {params: Object.assign(params, searchWhere)}).then(res => {
					if (res.data.code == 0) {
						this.newsList = res.data.data.list;
						this.total = res.data.data.total;
						this.pageSize = Number(res.data.data.pageSize);
						this.totalPage = res.data.data.totalPage;
						if(this.pageSizes.length==0){
							this.pageSizes = [this.pageSize, this.pageSize*2, this.pageSize*3, this.pageSize*5];
						}
					}
				});
			},
			getHotList(){
				let params = {page:1, limit: 4,sort:'addtime',order:'desc'};
				this.$http.get('news/autoSort', {params: params}).then(res => {
					if (res.data.code == 0) {
						this.hotList = res.data.data.list;
					}
				});
			},
			curChange(page) {
				this.getNewsList(page);
			},
			prevClick(page) {
				this.getNewsList(page);
			},
			nextClick(page) {
				this.getNewsList(page);
			},
			toNewsDetail(item) {
				this.$router.push({path: '/index/newsDetail', query: {id: item.id}});
			}
		}
	}
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
	.news-preview-pv {
				margin: 0px auto;
				color: #333;
				background: none;
				width: 1200px;
				font-size: 16px;
				position: relative;
				.list-form-pv {
						padding: 10px;
						background: none;
						display: flex;
						width: 100%;
						justify-content: center;
						align-items: center;
						flex-wrap: wrap;
						height: auto;
						.search-item {
								margin: 0 10px;
								.el-input {
										width: 100%;
									}
				.el-input /deep/ .el-input__inner {
										border: 1px solid #ccc;
										border-radius: 4px;
										padding: 0 10px;
										margin: 0;
										color: #333;
										width: auto;
										font-size: 16px;
										line-height: 42px;
										min-width: 350px;
										height: 42px;
									}
			}
			.search-btn {
								cursor: pointer;
								border: 0;
								border-radius: 4px;
								padding: 0px 15px;
								margin: 0 10px 0 0;
								color: #fff;
								background: #03abe9;
								width: auto;
								font-size: inherit;
								line-height: 42px;
								height: 42px;
								.icon {
										margin: 0 3px 0 0;
										color: #fff;
										font-size: inherit;
									}
			}
		}
		.category-list {
						padding: 0 10px;
						margin: 30px auto;
						background: none;
						display: flex;
						width: 100%;
						height: auto;
						.item {
								cursor: pointer;
								border-radius: 4px;
								padding: 0 10px;
								margin: 0 10px 0 0;
								color: #333;
								background: none;
								width: auto;
								font-size: inherit;
								line-height: 36px;
								text-align: center;
								min-width: 80px;
							}
			
			.item:hover {
								color: #fff;
								background: #03abe9;
							}
			
			.item.active {
								color: #fff;
								background: #03abe9;
							}
		}
		.list12 {
						padding: 0 10px 30px;
						width: 100%;
						.list-item1 {
								border: 0px solid #E6E6E6;
								padding: 20px 20px;
								margin: 0 auto;
								overflow: hidden;
								max-width: 100%;
								background: url(http://codegen.caihongy.cn/20240918/0158f8ec08364ef389a696ea5ad88d08.png) no-repeat center top,#018cc020;
								width: 100%;
								transition: all 0.6s;
								.img {
										max-height: 400px;
										overflow: hidden;
										width: 44%;
										float: left;
										height: 364px;
										img {
												object-fit: cover;
												width: 100%;
												transition: all 0.6s;
												height: 364px;
											}
				}
				.infoBox {
										padding: 52px 32px 0 30px;
										overflow: hidden;
										width: 55%;
										box-sizing: border-box;
										float: left;
										.name {
												color: #333;
												font-weight: 600;
												font-size: 20px;
												line-height: 36px;
											}
					.desc {
												margin: 15px 0 0 0;
												overflow: hidden;
												color: #333;
												font-weight: 400;
												display: -webkit-box;
												font-size: inherit;
												line-height: 32px;
												text-overflow: ellipsis;
												position: relative;
												-webkit-box-orient: vertical;
												-webkit-line-clamp: 2;
											}
					.infoCenter {
												margin: 20px 0 0;
												color: #333;
												display: flex;
												width: 100%;
												flex-wrap: wrap;
												.time_item {
														padding: 0;
														margin: 0 5px 0 0;
														.icon {
																margin: 0 2px 0 0;
																color: inherit;
																font-size: inherit;
																line-height: 1.5;
															}
							.label {
																color: inherit;
																font-size: inherit;
																line-height: 1.5;
															}
							.text {
																color: inherit;
																font-size: inherit;
																line-height: 1.5;
															}
						}
						.publisher_item {
														padding: 0;
														margin: 0 5px 0 0;
														.icon {
																margin: 0 2px 0 0;
																color: inherit;
																font-size: inherit;
																line-height: 1.5;
															}
							.label {
																color: inherit;
																font-size: inherit;
																line-height: 1.5;
															}
							.text {
																color: inherit;
																font-size: inherit;
																line-height: 1.5;
															}
						}
						.like_item {
														padding: 0;
														margin: 0 5px 0 0;
														.icon {
																margin: 0 2px 0 0;
																color: inherit;
																font-size: inherit;
																line-height: 1.5;
															}
							.label {
																color: inherit;
																font-size: inherit;
																line-height: 1.5;
															}
							.text {
																color: inherit;
																font-size: inherit;
																line-height: 1.5;
															}
						}
						.collect_item {
														padding: 0;
														margin: 0 5px 0 0;
														.icon {
																margin: 0 2px 0 0;
																color: inherit;
																font-size: inherit;
																line-height: 1.5;
															}
							.label {
																color: inherit;
																font-size: inherit;
																line-height: 1.5;
															}
							.text {
																color: inherit;
																font-size: inherit;
																line-height: 1.5;
															}
						}
						.view_item {
														padding: 0;
														.icon {
																margin: 0 2px 0 0;
																color: inherit;
																font-size: inherit;
																line-height: 1.5;
															}
							.label {
																color: inherit;
																font-size: inherit;
																line-height: 1.5;
															}
							.text {
																color: inherit;
																font-size: inherit;
																line-height: 1.5;
															}
						}
					}
					.more_btn {
												border: 0px solid #ccc;
												cursor: pointer;
												border-radius: 23px;
												margin: 52px 0;
												overflow: hidden;
												color: #666;
												background: #fff;
												display: block;
												width: 140px;
												line-height: 44px;
												text-align: center;
												height: 44px;
												.text {
														color: inherit;
														font-size: 16px;
													}
						.icon {
														color: inherit;
														font-size: 12px;
													}
					}
				}
			}
			.list-item1:hover {
								cursor: pointer;
								.img {
					img {
												transform: scale(1.05);
											}
				}
				.infoBox {
					.name {
												color: #03abe9;
											}
					.desc {
												color: #000;
											}
					.infoCenter {
						.time_item {
							.icon {
																color: #000;
															}
							.label {
																color: #000;
															}
							.text {
																color: #000;
															}
						}
						.publisher_item {
							.icon {
																color: #000;
															}
							.label {
																color: #000;
															}
							.text {
																color: #000;
															}
						}
						.like_item {
							.icon {
																color: #000;
															}
							.label {
																color: #000;
															}
							.text {
																color: #000;
															}
						}
						.collect_item {
							.icon {
																color: #000;
															}
							.label {
																color: #000;
															}
							.text {
																color: #000;
															}
						}
						.view_item {
							.icon {
																color: #000;
															}
							.label {
																color: #000;
															}
							.text {
																color: #000;
															}
						}
					}
					.more_btn {
												border: 0px solid #03abe9;
												background: #03abe9;
												.text {
														color: #fff;
													}
						.icon {
														color: #fff;
													}
					}
				}
			}
			.list-body {
								margin: 30px auto 0;
								overflow: hidden;
								width: 100%;
								.list-body-left {
										overflow: hidden;
										width: 25.6%;
										box-sizing: border-box;
										float: left;
										.list-item {
												cursor: pointer;
												padding: 0px 0 0px;
												margin: 0 0 0px;
												overflow: hidden;
												display: block;
												width: 100%;
												.img {
														overflow: hidden;
														width: 100%;
														text-align: center;
														height: auto;
														img {
																max-height: 100%;
																max-width: 100%;
																object-fit: cover;
																display: inline-block;
																width: 100%;
																transition: all 0.6s;
																height: 150px;
															}
						}
						.name {
														margin: 0px auto;
														overflow: hidden;
														color: #333;
														font-weight: 500;
														display: -webkit-box;
														width: 100%;
														font-size: inherit;
														line-height: 40px;
														text-overflow: ellipsis;
														-webkit-box-orient: vertical;
														-webkit-line-clamp: 1;
														transition: all 0.6s;
													}
					}
					.list-item:hover {
												border-color: #0782ff30;
												.img {
							img {
																transform: scale(1.05);
															}
						}
						.name {
														color: #03abe9;
													}
					}
				}
				.list-body-right {
										border: 1px solid #E6E6E6;
										padding: 0 0 0px 55px;
										width: 68.8%;
										border-width: 0 0 0 1px;
										box-sizing: border-box;
										float: right;
										.list-item {
												cursor: pointer;
												border: 1px solid #E6E6E6;
												padding: 0px 0 0px;
												margin: 0 0 20px;
												overflow: hidden;
												display: block;
												width: 100%;
												border-width: 0 0 1px;
												.infoBox {
														width: 84%;
														float: left;
														.name {
																overflow: hidden;
																color: #333;
																white-space: nowrap;
																font-weight: 700;
																font-size: inherit;
																line-height: 30px;
																text-overflow: ellipsis;
																transition: all 0.6s;
															}
							.desc {
																margin: 10px 0 20px;
																overflow: hidden;
																color: #999;
																font-weight: 400;
																display: -webkit-box;
																font-size: inherit;
																line-height: 2;
																text-overflow: ellipsis;
																position: relative;
																-webkit-box-orient: vertical;
																-webkit-line-clamp: 2;
																transition: all 0.6s;
															}
						}
						.time_item {
														border: 0px solid #E6E6E6;
														padding: 0 10px;
														margin: 15px 0 0;
														float: right;
														text-align: center;
														.day {
																border: 1px solid #E6E6E6;
																padding: 0px 3px;
																color: #888;
																font-weight: 400;
																font-size: 20px;
																border-width: 0 0 1px;
																line-height: 40px;
																transition: all 0s;
															}
							.year {
																border: none;
																color: #888;
																font-weight: 400;
																font-size: 20px;
																line-height: 40px;
																transition: all 0s;
															}
						}
					}
					.list-item:hover {
												border-color: #03abe930;
												.infoBox {
							.name {
																color: #03abe9;
															}
							.desc {
																color: #000;
															}
						}
						.time_item {
														.day {
																color: #03abe9;
																border-color: #03abe930;
															}
							.year {
																color: #03abe9;
															}
						}
					}
				}
			}
		}
		.hot {
						background: none;
						width: 100%;
						height: auto;
						order: 80;
						.hot-title {
								padding: 0 0 0 130px;
								color: #fff;
								background: url(http://codegen.caihongy.cn/20240918/5be766ae35ab449c88028d0dc390cf47.png) no-repeat left center / 100% 100%;
								width: 100%;
								font-size: 24px;
								line-height: 65px;
							}
			.hot-list {
								padding: 0;
								background: none;
								width: 100%;
								height: auto;
								.hot-item {
										cursor: pointer;
										padding: 0;
										margin: 20px 10px;
										background: #fff;
										display: inline-block;
										width: calc(25% - 20px);
										height: auto;
										img {
												object-fit: cover;
												display: block;
												width: 100%;
												height: 150px;
											}
					.hot-name {
												padding: 4px 5px 0;
												overflow: hidden;
												color: inherit;
												white-space: nowrap;
												width: 100%;
												font-size: inherit;
												line-height: 30px;
												text-overflow: ellipsis;
											}
					.hot-time {
												padding: 0 5px;
												color: #999;
												font-weight: 500;
												font-size: inherit;
												line-height: 24px;
												text-align: right;
											}
				}
			}
		}
	}
	
	.index-pv1 .animation-box {
		transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
		z-index: initial;
	}
	
	.index-pv1 .animation-box:hover {
				transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				-webkit-perspective: 1000px;
				perspective: 1000px;
				transition: 0.3s;
				z-index: 1;
	}
	
	.index-pv1 .animation-box img {
		transform: rotate(0deg) scale(1) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
	}
	
	.index-pv1 .animation-box img:hover {
				transform: rotate(0deg) scale(0.98) skew(0deg, 0deg) translate3d(0px, 0px, 0px);
				-webkit-perspective: 1000px;
				perspective: 1000px;
				transition: 0.3s;
			}
</style>

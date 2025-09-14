<template>
	<div>

		<div class="container">
			<el-form class='rgs-form animate__animated animate__' v-if="pageFlag=='register'" ref="registerForm" :model="registerForm" :rules="rules">
				<div class="rgs-form2">
					<div class="title">中小学生情绪管理平台</p></div>
					<el-form-item class="list-item" v-if="tableName=='xuesheng'" prop="xueshengxuehao">
						<div class="label" :class="changeRules('xueshengxuehao')?'required':''">学生学号：</div>
						<el-input v-model="registerForm.xueshengxuehao"  placeholder="请输入学生学号" />
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='xuesheng'" prop="mima">
						<div class="label" :class="changeRules('mima')?'required':''">密码：</div>
						<el-input v-model="registerForm.mima" type="password" placeholder="请输入密码" />
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='xuesheng'" prop="mima2">
						<div class="label" :class="changeRules('mima')?'required':''">确认密码：</div>
						<el-input v-model="registerForm.mima2" type="password" placeholder="请再次输入密码" />
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='xuesheng'" prop="xueshengxingming">
						<div class="label" :class="changeRules('xueshengxingming')?'required':''">学生姓名：</div>
						<el-input v-model="registerForm.xueshengxingming"  placeholder="请输入学生姓名" />
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='xuesheng'" prop="xingbie">
						<div class="label" :class="changeRules('xingbie')?'required':''">性别：</div>
						<el-select v-model="registerForm.xingbie" placeholder="请选择性别" >
							<el-option
								v-for="(item,index) in xueshengxingbieOptions"
								:key="index"
								:label="item"
								:value="item">
							</el-option>
						</el-select>
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='xuesheng'" prop="nianling">
						<div class="label" :class="changeRules('nianling')?'required':''">年龄：</div>
						<el-input v-model.number="registerForm.nianling"  placeholder="请输入年龄" />
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='xuesheng'" prop="xueshengshouji">
						<div class="label" :class="changeRules('xueshengshouji')?'required':''">学生手机：</div>
						<el-input v-model="registerForm.xueshengshouji"  placeholder="请输入学生手机" />
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='xuesheng'" prop="touxiang">
						<div class="label" :class="changeRules('touxiang')?'required':''">头像：</div>
						<file-upload
							tip="点击上传头像"
							action="file/upload"
							:limit="1"
							:multiple="true"
							:fileUrls="registerForm.touxiang?registerForm.touxiang:''"
							@change="xueshengtouxiangUploadChange"
						></file-upload>
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='xinliyisheng'" prop="yishenggonghao">
						<div class="label" :class="changeRules('yishenggonghao')?'required':''">教师工号：</div>
						<el-input v-model="registerForm.yishenggonghao"  placeholder="请输入教师工号" />
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='xinliyisheng'" prop="mima">
						<div class="label" :class="changeRules('mima')?'required':''">密码：</div>
						<el-input v-model="registerForm.mima" type="password" placeholder="请输入密码" />
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='xinliyisheng'" prop="mima2">
						<div class="label" :class="changeRules('mima')?'required':''">确认密码：</div>
						<el-input v-model="registerForm.mima2" type="password" placeholder="请再次输入密码" />
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='xinliyisheng'" prop="yishengxingming">
						<div class="label" :class="changeRules('yishengxingming')?'required':''">教师姓名：</div>
						<el-input v-model="registerForm.yishengxingming"  placeholder="请输入教师姓名" />
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='xinliyisheng'" prop="xingbie">
						<div class="label" :class="changeRules('xingbie')?'required':''">性别：</div>
						<el-select v-model="registerForm.xingbie" placeholder="请选择性别" >
							<el-option
								v-for="(item,index) in xinliyishengxingbieOptions"
								:key="index"
								:label="item"
								:value="item">
							</el-option>
						</el-select>
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='xinliyisheng'" prop="zhaopian">
						<div class="label" :class="changeRules('zhaopian')?'required':''">照片：</div>
						<file-upload
							tip="点击上传照片"
							action="file/upload"
							:limit="1"
							:multiple="true"
							:fileUrls="registerForm.zhaopian?registerForm.zhaopian:''"
							@change="xinliyishengzhaopianUploadChange"
						></file-upload>
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='xinliyisheng'" prop="zhicheng">
						<div class="label" :class="changeRules('zhicheng')?'required':''">职称：</div>
						<el-input v-model="registerForm.zhicheng"  placeholder="请输入职称" />
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='xinliyisheng'" prop="lianxidianhua">
						<div class="label" :class="changeRules('lianxidianhua')?'required':''">联系电话：</div>
						<el-input v-model="registerForm.lianxidianhua"  placeholder="请输入联系电话" />
					</el-form-item>
					<el-form-item class="list-item" v-if="tableName=='xinliyisheng'" prop="youxiang">
						<div class="label" :class="changeRules('youxiang')?'required':''">邮箱：</div>
						<el-input v-model="registerForm.youxiang"  placeholder="请输入邮箱" />
					</el-form-item>
					<div class="register-btn">
						<div class="register-btn1">
							<el-button class="register_btn" type="primary" @click="submitForm('registerForm')">注册</el-button>
						</div>
						<div class="register-btn2">
							<router-link class="has_btn" to="/login">已有账号，直接登录</router-link>
						</div>
					</div>
				</div>
				<div class="idea1"></div>
				<div class="idea2"></div>
			</el-form>
		</div>
	</div>
</div>
</template>

<script>
	import 'animate.css';

export default {
    //数据集合
    data() {
		return {
            pageFlag : '',
			tableName: '',
			registerForm: {},
			forgetForm: {},
			rules: {},
			requiredRules: {},
            xueshengxingbieOptions: [],
            xinliyishengxingbieOptions: [],
		}
    },
	mounted() {
		if(this.$route.query.pageFlag=='register'){
			this.tableName = this.$route.query.role;
			if(this.tableName=='xuesheng'){
				this.registerForm = {
					xueshengxuehao: '',
					mima: '',
					mima2: '',
					xueshengxingming: '',
					xingbie: '',
					nianling: '',
					xueshengshouji: '',
					touxiang: '',
				}
			}
			if(this.tableName=='xinliyisheng'){
				this.registerForm = {
					yishenggonghao: '',
					mima: '',
					mima2: '',
					yishengxingming: '',
					xingbie: '',
					zhaopian: '',
					zhicheng: '',
					lianxidianhua: '',
					youxiang: '',
				}
			}
			if ('xuesheng' == this.tableName) {
				this.rules.xueshengxuehao = [{ required: true, message: '请输入学生学号', trigger: 'blur' }];
				this.requiredRules.xueshengxuehao = [{ required: true, message: '请输入学生学号', trigger: 'blur' }]
			}
			if ('xuesheng' == this.tableName) {
				this.rules.mima = [{ required: true, message: '请输入密码', trigger: 'blur' }];
				this.requiredRules.mima = [{ required: true, message: '请输入密码', trigger: 'blur' }]
			}
			if ('xuesheng' == this.tableName) {
				this.rules.xueshengxingming = [{ required: true, message: '请输入学生姓名', trigger: 'blur' }];
				this.requiredRules.xueshengxingming = [{ required: true, message: '请输入学生姓名', trigger: 'blur' }]
			}
			this.xueshengxingbieOptions = "男,女".split(',');
			if ('xuesheng' == this.tableName) {
				this.rules.nianling = [{ required: true, validator: this.$validate.isIntNumer, trigger: 'blur' }];
			}
			if ('xuesheng' == this.tableName) {
				this.rules.xueshengshouji = [{ required: true, validator: this.$validate.isMobileNotNull, trigger: 'blur' }];
				this.requiredRules.xueshengshouji = [{ required: true, message: '请输入学生手机', trigger: 'blur' }]
			}
			if ('xuesheng' == this.tableName) {
				this.rules.touxiang = [{ required: true, message: '请输入头像', trigger: 'blur' }];
				this.requiredRules.touxiang = [{ required: true, message: '请输入头像', trigger: 'blur' }]
			}
			if ('xinliyisheng' == this.tableName) {
				this.rules.yishenggonghao = [{ required: true, message: '请输入教师工号', trigger: 'blur' }];
				this.requiredRules.yishenggonghao = [{ required: true, message: '请输入教师工号', trigger: 'blur' }]
			}
			if ('xinliyisheng' == this.tableName) {
				this.rules.mima = [{ required: true, message: '请输入密码', trigger: 'blur' }];
				this.requiredRules.mima = [{ required: true, message: '请输入密码', trigger: 'blur' }]
			}
			if ('xinliyisheng' == this.tableName) {
				this.rules.yishengxingming = [{ required: true, message: '请输入教师姓名', trigger: 'blur' }];
				this.requiredRules.yishengxingming = [{ required: true, message: '请输入教师姓名', trigger: 'blur' }]
			}
			this.xinliyishengxingbieOptions = "男,女".split(',');
			if ('xinliyisheng' == this.tableName) {
				this.rules.lianxidianhua = [{ required: true, validator: this.$validate.isMobile, trigger: 'blur' }];
			}
			if ('xinliyisheng' == this.tableName) {
				this.rules.youxiang = [{ required: true, validator: this.$validate.isEmail, trigger: 'blur' }];
			}
		}
	},
    created() {
		this.pageFlag = this.$route.query.pageFlag;
    },
    //方法集合
    methods: {
		changeRules(name){
			if(this.requiredRules[name]){
				return true
			}
			return false
		},
		// 获取uuid
		getUUID () {
			return new Date().getTime();
		},
        // 下二随
		xueshengtouxiangUploadChange(fileUrls) {
			this.registerForm.touxiang = fileUrls.replace(new RegExp(this.$config.baseUrl,"g"),"");
		},
		xinliyishengzhaopianUploadChange(fileUrls) {
			this.registerForm.zhaopian = fileUrls.replace(new RegExp(this.$config.baseUrl,"g"),"");
		},

		// 多级联动参数


		submitForm(formName) {
			this.$refs[formName].validate((valid) => {
				if (valid) {
					var url=this.tableName+"/register";
					if(`xuesheng` == this.tableName && this.registerForm.mima!=this.registerForm.mima2) {
						this.$message.error(`两次密码输入不一致`);
						return
					}
					if(`xinliyisheng` == this.tableName && this.registerForm.mima!=this.registerForm.mima2) {
						this.$message.error(`两次密码输入不一致`);
						return
					}
					this.$http.post(url, this.registerForm).then(res => {
						if (res.data.code === 0) {
							this.$message({
								message: '注册成功',
								type: 'success',
								duration: 1500,
								onClose: () => {
									this.$router.push('/login');
								}
							});
						} else {
							this.$message.error(res.data.msg);
						}
					});
				} else {
					return false;
				}
			});
		},
		resetForm(formName) {
			this.$refs[formName].resetFields();
		}
    }
}
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
	.container {
		background-repeat: no-repeat;
		background-size: 100% 100%!important;
		background: url(http://codegen.caihongy.cn/20240919/6ea62b3c9bbb4010b3c8a88b1efb2c49.jpg);
		display: flex;
		width: 100%;
		min-height: 100vh;
		justify-content: center;
		align-items: center;
		background-position: center center;
		position: relative;
		background: url(http://codegen.caihongy.cn/20240919/6ea62b3c9bbb4010b3c8a88b1efb2c49.jpg);
		.rgs-form {
			padding: 0;
			margin: 0;
			z-index: 10;
			background: url(http://codegen.caihongy.cn/20241025/c7d9f80e41c64ee4990c2926b5f29aa9.png) no-repeat center center / 100% 100%;
			display: flex;
			width: 100%;
			min-height: 100vh;
			justify-content: flex-start;
			align-items: center;
			height: auto;
			.rgs-form2 {
				padding: 20px 60px 0 0;
				margin: 0 0 0 10%;
				background: none;
				width: 660px;
				.title {
					margin: 0 0 20px 0;
					color: #333;
					width: 100%;
					font-size: 20px;
					line-height: 44px;
					text-align: center;
				}
				.subtitle {
					margin: 0 0 10px 0;
					text-shadow: 4px 4px 2px rgba(64, 158, 255, .5);
					color: rgba(64, 158, 255, 1);
					width: 100%;
					font-size: 20px;
					line-height: 44px;
					text-align: center;
				}
				.list-item {
					margin: 0 auto 25px;
					width: 100%;
					/deep/.el-form-item__content {
						padding: 0 0 0 120px;
						display: block;
						width: calc(100% - 0px);
						.label {
							padding: 0 5px 0 0;
							z-index: 9;
							color: #333;
							left: 0;
							width: 120px;
							font-size: 16px;
							line-height: 40px;
							position: absolute !important;
							text-align: right;
						}
						
						.required {
							position: relative;
						}
						.required::after{
							margin: 0 10px 0 0;
							color: red;
							left: 110px;
							position: inherit;
							content: "*";
						}
						.el-input {
							flex: 1;
							width: 100%;
						}
						.el-input .el-input__inner {
							border: 1px solid #ddd;
							border-radius: 0;
							padding: 0 10px;
							color: #666;
							flex: 1;
							width: calc(100% - 0px);
							font-size: 15px;
							height: 40px;
						}
						.el-input .el-input__inner:focus {
							border: 1px solid #f7db61;
							border-radius: 0;
							padding: 0 10px;
							outline: none;
							color: #666;
							width: calc(100% - 0px);
							font-size: 15px;
							height: 40px;
						}
						.el-input-number {
							flex: 1;
							width: 100%;
						}
						.el-input-number /deep/ .el-input__inner {
							text-align: left;
							border: 1px solid #ddd;
							border-radius: 0;
							padding: 0 10px;
							color: #666;
							flex: 1;
							width: calc(100% - 0px);
							font-size: 15px;
							height: 40px;
						}
						.el-input-number /deep/ .el-input-number__decrease {
							display: none;
						}
						.el-input-number /deep/ .el-input-number__increase {
							display: none;
						}
						.el-select {
							flex: 1;
							width: calc(100% - 0px);
						}
						.el-select .el-input__inner {
							border: 1px solid #ddd;
							border-radius: 0;
							padding: 0 10px;
							color: #666;
							width: 100%;
							font-size: 15px;
							height: 40px;
						}
						.el-select .el-input__inner:focus {
							border: 1px solid #f7db61;
							border-radius: 0;
							padding: 0 10px;
							outline: none;
							color: #666;
							width: 100%;
							font-size: 15px;
							height: 40px;
						}
						.el-date-editor {
							flex: 1;
							width: calc(100% - 0px);
						}
						.el-date-editor .el-input__inner {
							border: 1px solid #ddd;
							border-radius: 0;
							padding: 0 10px 0 30px;
							color: #666;
							width: 100%;
							font-size: 15px;
							height: 40px;
						}
						.el-date-editor .el-input__inner:focus {
							border: 1px solid #f7db61;
							border-radius: 0;
							padding: 0 10px 0 30px;
							outline: none;
							color: #666;
							width: 100%;
							font-size: 15px;
							height: 40px;
						}
						.el-upload--picture-card {
							background: transparent;
							border: 0;
							border-radius: 0;
							width: auto;
							height: auto;
							line-height: initial;
							vertical-align: middle;
						}
						.upload .upload-img {
							border: 1px solid #ddd;
							cursor: pointer;
							border-radius: 0px;
							color: #999;
							background: #fff;
							width: 80px;
							font-size: 24px;
							line-height: 60px;
							text-align: center;
							height: 60px;
						}
						.el-upload-list .el-upload-list__item {
							border: 1px solid #ddd;
							cursor: pointer;
							border-radius: 0px;
							color: #999;
							background: #fff;
							width: 80px;
							font-size: 24px;
							line-height: 60px;
							text-align: center;
							height: 60px;
							font-size: 14px;
							line-height: 1.8;
						}
						.el-upload .el-icon-plus {
							border: 1px solid #ddd;
							cursor: pointer;
							border-radius: 0px;
							color: #999;
							background: #fff;
							width: 80px;
							font-size: 24px;
							line-height: 60px;
							text-align: center;
							height: 60px;
						}
						.el-upload__tip {
							color: #666;
							font-size: 15px;
						}
						.emailInput {
							border: 1px solid #ddd;
							border-radius: 0px 0 0 0px;
							padding: 0 10px;
							margin: 0;
							color: #606266;
							background: #fff;
							flex: 1;
							width: calc(100% - 0px);
							font-size: 15px;
							height: 40px;
						}
						.emailInput:focus {
							border: 1px solid #f7db61;
							border-radius: 0px 0 0 0px;
							padding: 0 10px;
							outline: none;
							color: #606266;
							width: calc(100% - 0px);
							font-size: 15px;
							height: 40px;
						}
						.el-btn {
							border: 1px solid #ddd;
							cursor: pointer;
							border-radius: 0 0px 0px 0;
							padding: 0 10px;
							margin: 0;
							color: #333;
							background: #f5f5f5;
							width: 110px;
							font-size: 15px;
							float: right;
							height: 40px;
						}
						.el-btn:hover {
							opacity: 0.8;
						}
						
						.el-input__inner::placeholder {
							color: #999;
							font-size: 15px;
						}
						input::placeholder {
							color: #999;
							font-size: 15px;
						}
						.editor {
							margin: 0 0 0 0px;
							background: #fff;
							width: calc(100% - 0px);
							height: auto;
						}
					}
				}
				.register-btn {
					margin: 20px auto;
					width: 100%;
				}
				.register-btn1 {
					padding: 0 0 0 120px;
					width: 100%;
				}
				.register-btn2 {
					padding: 0 0 0 120px;
					margin: 10px auto;
					width: 100%;
					text-align: right;
				}
				.register_btn {
					border: 0;
					cursor: pointer;
					border-radius: 4px;
					padding: 0 30px;
					margin: 0 0px;
					color: #fff;
					background: #03abe9;
					width: 100%;
					font-size: 16px;
					height: 40px;
				}
				.register_btn:hover {
					opacity: 0.8;
				}
				.has_btn {
					cursor: pointer;
					padding: 0;
					color: #555;
					display: inline-block;
					text-decoration: none;
					font-size: 15px;
					line-height: 40px;
				}
				.has_btn:hover {
					opacity: 0.8;
				}
			}
			.idea1 {
				background: red;
				display: none;
				width: 100%;
				height: 40px;
			}
			.idea2 {
				background: blue;
				display: none;
				width: 100%;
				height: 40px;
			}
		}
	}
	
	::-webkit-scrollbar {
		display: none;
	}
</style>

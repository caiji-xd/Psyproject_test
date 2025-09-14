# coding:utf-8
import random
from datetime import datetime
from sqlalchemy import text,TIMESTAMP

from api.models.models import Base_model
from api.exts import db
from sqlalchemy.dialects.mysql import DOUBLE,LONGTEXT
class xinliyisheng(Base_model):
    __doc__ = u'''xinliyisheng'''
    __tablename__ = 'xinliyisheng'

    __loginUser__='yishenggonghao'


    __authTables__={}
    __authPeople__='是'
    __authSeparate__='否'
    __thumbsUp__='否'
    __intelRecom__='否'
    __browseClick__='否'
    __foreEndListAuth__='否'
    __foreEndList__='否'
    __isAdmin__='否'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    yishenggonghao=db.Column( db.VARCHAR(255), nullable=False,unique=False,comment='医生工号' )
    mima=db.Column( db.VARCHAR(255), nullable=False,unique=False,comment='密码' )
    yishengxingming=db.Column( db.VARCHAR(255), nullable=False,unique=False,comment='医生姓名' )
    xingbie=db.Column( db.VARCHAR(255), nullable=False,unique=False,comment='性别' )
    zhaopian=db.Column( db.Text,  nullable=True, unique=False,comment='照片' )
    zhicheng=db.Column( db.VARCHAR(255), nullable=False,unique=False,comment='职称' )
    lianxidianhua=db.Column( db.VARCHAR(255), nullable=False,unique=False,comment='联系电话' )
    youxiang=db.Column( db.VARCHAR(255), nullable=False,unique=False,comment='邮箱' )
class xuesheng(Base_model):
    __doc__ = u'''xuesheng'''
    __tablename__ = 'xuesheng'

    __loginUser__='xueshengxuehao'


    __authTables__={}
    __authPeople__='是'
    __authSeparate__='否'
    __thumbsUp__='否'
    __intelRecom__='否'
    __browseClick__='否'
    __foreEndListAuth__='否'
    __foreEndList__='否'
    __isAdmin__='否'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    xueshengxuehao=db.Column( db.VARCHAR(255), nullable=False,unique=False,comment='学生学号' )
    mima=db.Column( db.VARCHAR(255), nullable=False,unique=False,comment='密码' )
    xueshengxingming=db.Column( db.VARCHAR(255), nullable=False,unique=False,comment='学生姓名' )
    xingbie=db.Column( db.VARCHAR(255), nullable=False,unique=False,comment='性别' )
    nianling=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='年龄' )
    xueshengshouji=db.Column( db.VARCHAR(255), nullable=False,unique=False,comment='学生手机' )
    touxiang=db.Column( db.Text,  nullable=True, unique=False,comment='头像' )

class aboutus(Base_model):
    __doc__ = u'''aboutus'''
    __tablename__ = 'aboutus'



    __authTables__={}
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    title=db.Column( db.VARCHAR(255), nullable=False,unique=False,comment='标题' )
    subtitle=db.Column( db.VARCHAR(255), nullable=False,unique=False,comment='副标题' )
    content=db.Column( db.Text,  nullable=True, unique=False,comment='内容' )
    picture1=db.Column( db.Text,  nullable=True, unique=False,comment='图片1' )
    picture2=db.Column( db.Text,  nullable=True, unique=False,comment='图片2' )
    picture3=db.Column( db.Text,  nullable=True, unique=False,comment='图片3' )

class exampaper(Base_model):
    __doc__ = u'''exampaper'''
    __tablename__ = 'exampaper'



    __authTables__={}

    __authPeople__='否'
    __authSeparate__='否'
    __thumbsUp__='否'
    __intelRecom__='否'
    __browseClick__='否'
    __foreEndListAuth__='否'
    __foreEndList__='否'
    __isAdmin__='否'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    name=db.Column( db.VARCHAR(255), nullable=False,unique=False,comment='心理测试名称' )
    time=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='心理测试时长(分钟)' )
    status=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='心理测试状态' )

class examquestion(Base_model):
    __doc__ = u'''examquestion'''
    __tablename__ = 'examquestion'



    __authTables__={}

    __authPeople__='否'
    __authSeparate__='否'
    __thumbsUp__='否'
    __intelRecom__='否'
    __browseClick__='否'
    __foreEndListAuth__='否'
    __foreEndList__='否'
    __isAdmin__='否'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    paperid=db.Column( db.BigInteger, nullable=False, unique=False,comment='所属心理测试id（外键）' )
    papername=db.Column( db.VARCHAR(255), nullable=False,unique=False,comment='心理测试名称' )
    questionname=db.Column( db.VARCHAR(255), nullable=False,unique=False,comment='试题名称' )
    options=db.Column( db.Text,  nullable=True, unique=False,comment='选项，json字符串' )
    score=db.Column( db.BigInteger, nullable=False, unique=False,comment='分值' )
    answer=db.Column( db.VARCHAR(255), nullable=False,unique=False,comment='正确答案' )
    analysis=db.Column( db.Text,  nullable=True, unique=False,comment='答案解析' )
    type=db.Column( db.BigInteger, nullable=False, unique=False,comment='试题类型，0：单选题 1：多选题 2：判断题 3：填空题（暂不考虑多项填空）4:主观题' )
    sequence=db.Column( db.BigInteger, nullable=False, unique=False,comment='试题排序，值越大排越前面' )

class examquestionbank(Base_model):
    __doc__ = u'''examquestionbank'''
    __tablename__ = 'examquestionbank'



    __authTables__={}

    __authPeople__='否'
    __authSeparate__='否'
    __thumbsUp__='否'
    __intelRecom__='否'
    __browseClick__='否'
    __foreEndListAuth__='否'
    __foreEndList__='否'
    __isAdmin__='否'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    questionname=db.Column( db.VARCHAR(255), nullable=False,unique=False,comment='试题名称' )
    options=db.Column( db.Text,  nullable=True, unique=False,comment='选项，json字符串' )
    score=db.Column( db.BigInteger, nullable=False, unique=False,comment='分值' )
    answer=db.Column( db.VARCHAR(255), nullable=False,unique=False,comment='正确答案' )
    analysis=db.Column( db.Text,  nullable=True, unique=False,comment='答案解析' )
    type=db.Column( db.BigInteger, nullable=False, unique=False,comment='试题类型，0：单选题 1：多选题 2：判断题 3：填空题（暂不考虑多项填空） 4:主观题' )
    sequence=db.Column( db.BigInteger, nullable=False, unique=False,comment='试题排序，值越大排越前面' )

class examrecord(Base_model):
    __doc__ = u'''examrecord'''
    __tablename__ = 'examrecord'



    __authTables__={}

    __authPeople__='否'
    __authSeparate__='否'
    __thumbsUp__='否'
    __intelRecom__='否'
    __browseClick__='否'
    __foreEndListAuth__='否'
    __foreEndList__='否'
    __isAdmin__='否'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    userid=db.Column( db.BigInteger, nullable=False, unique=False,comment='用户id' )
    username=db.Column( db.VARCHAR(255), nullable=False,unique=False,comment='用户名' )
    paperid=db.Column( db.BigInteger, nullable=False, unique=False,comment='心理测试id（外键）' )
    papername=db.Column( db.VARCHAR(255), nullable=False,unique=False,comment='心理测试名称' )
    questionid=db.Column( db.BigInteger, nullable=False, unique=False,comment='试题id（外键）' )
    questionname=db.Column( db.VARCHAR(255), nullable=False,unique=False,comment='试题名称' )
    options=db.Column( db.Text,  nullable=True, unique=False,comment='选项，json字符串' )
    score=db.Column( db.BigInteger, nullable=False, unique=False,comment='分值' )
    answer=db.Column( db.VARCHAR(255), nullable=False,unique=False,comment='正确答案' )
    analysis=db.Column( db.Text,  nullable=True, unique=False,comment='答案解析' )
    ismark=db.Column( db.BigInteger, nullable=False, unique=False,comment='是否批卷' )
    type=db.Column( db.BigInteger, nullable=False, unique=False,comment='试题类型，0：单选题 1：多选题 2：判断题 3：填空题（暂不考虑多项填空） 4:主观题' )
    myscore=db.Column( db.BigInteger, nullable=False, unique=False,comment='试题得分' )
    myanswer=db.Column( db.VARCHAR(255), nullable=False,unique=False,comment='考生答案' )

class fudaoyuyue(Base_model):
    __doc__ = u'''fudaoyuyue'''
    __tablename__ = 'fudaoyuyue'



    __authTables__={'yishenggonghao':'xinliyisheng','xueshengxuehao':'xuesheng',}

    __authPeople__='否'
    __authSeparate__='否'
    __thumbsUp__='否'
    __intelRecom__='否'
    __browseClick__='否'
    __foreEndListAuth__='否'
    __foreEndList__='否'
    __isAdmin__='否'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    zhenshihao=db.Column( db.VARCHAR(255), nullable=False,unique=False,comment='诊室号' )
    fengmian=db.Column( db.Text,  nullable=True, unique=False,comment='封面' )
    keshihao=db.Column( db.VARCHAR(255), nullable=False,unique=False,comment='科室号' )
    keshimingcheng=db.Column( db.VARCHAR(255), nullable=False,unique=False,comment='科室名称' )
    menzhenleixing=db.Column( db.VARCHAR(255), nullable=False,unique=False,comment='门诊类型' )
    guahaofei=db.Column( db.VARCHAR(255), nullable=False,unique=False,comment='挂号费' )
    yishenggonghao=db.Column( db.VARCHAR(255), nullable=False,unique=False,comment='医生工号' )
    yishengxingming=db.Column( db.VARCHAR(255), nullable=False,unique=False,comment='医生姓名' )
    zhicheng=db.Column( db.VARCHAR(255), nullable=False,unique=False,comment='职称' )
    yishengjieshao=db.Column( db.Text,  nullable=True, unique=False,comment='医生介绍' )
    xueshengxuehao=db.Column( db.VARCHAR(255), nullable=False,unique=False,comment='学生学号' )
    xueshengxingming=db.Column( db.VARCHAR(255), nullable=False,unique=False,comment='学生姓名' )
    ispay=db.Column( db.VARCHAR(255), nullable=False,unique=False,comment='是否支付' )
    clicknum=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='点击次数' )

class messages(Base_model):
    __doc__ = u'''messages'''
    __tablename__ = 'messages'



    __authTables__={}
    __hasMessage__='是'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    userid=db.Column( db.BigInteger, nullable=False, unique=False,comment='留言人id' )
    username=db.Column( db.VARCHAR(255), nullable=False,unique=False,comment='用户名' )
    avatarurl=db.Column( db.Text,  nullable=True, unique=False,comment='头像' )
    content=db.Column( db.Text,  nullable=True, unique=False,comment='留言内容' )
    cpicture=db.Column( db.Text,  nullable=True, unique=False,comment='留言图片' )
    reply=db.Column( db.Text,  nullable=True, unique=False,comment='回复内容' )
    rpicture=db.Column( db.Text,  nullable=True, unique=False,comment='回复图片' )

class news(Base_model):
    __doc__ = u'''news'''
    __tablename__ = 'news'



    __authTables__={}
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    title=db.Column( db.VARCHAR(255), nullable=False,unique=False,comment='标题' )
    introduction=db.Column( db.Text,  nullable=True, unique=False,comment='简介' )
    typename=db.Column( db.VARCHAR(255), nullable=False,unique=False,comment='分类名称' )
    name=db.Column( db.VARCHAR(255), nullable=False,unique=False,comment='发布人' )
    headportrait=db.Column( db.Text,  nullable=True, unique=False,comment='头像' )
    clicknum=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='点击次数' )
    clicktime=db.Column( db.DateTime,  nullable=True, unique=False,comment='最近点击时间'  )
    thumbsupnum=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='赞' )
    crazilynum=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='踩' )
    storeupnum=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='收藏数' )
    picture=db.Column( db.Text,  nullable=True, unique=False,comment='图片' )
    content=db.Column( db.Text,  nullable=True, unique=False,comment='内容' )

class newstype(Base_model):
    __doc__ = u'''newstype'''
    __tablename__ = 'newstype'



    __authTables__={}

    __authPeople__='否'
    __authSeparate__='否'
    __thumbsUp__='否'
    __intelRecom__='否'
    __browseClick__='否'
    __foreEndListAuth__='否'
    __foreEndList__='否'
    __isAdmin__='否'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    typename=db.Column( db.VARCHAR(255), nullable=False,unique=False,comment='分类名称' )

class scoredetermination(Base_model):
    __doc__ = u'''scoredetermination'''
    __tablename__ = 'scoredetermination'



    __authTables__={}

    __authPeople__='否'
    __authSeparate__='否'
    __thumbsUp__='否'
    __intelRecom__='否'
    __browseClick__='否'
    __foreEndListAuth__='否'
    __foreEndList__='否'
    __isAdmin__='否'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    papername=db.Column( db.VARCHAR(255), nullable=False,unique=False,comment='测评名称' )
    paperid=db.Column( db.VARCHAR(255), nullable=False,unique=False,comment='试卷id' )
    score=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='分数' )
    determine=db.Column( db.Text,  nullable=True, unique=False,comment='建议' )
    analysis=db.Column( db.Text,  nullable=True, unique=False,comment='分析' )

class storeup(Base_model):
    __doc__ = u'''storeup'''
    __tablename__ = 'storeup'



    __authTables__={}
    __authSeparate__='是'
    __foreEndListAuth__='是'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    userid=db.Column( db.BigInteger, nullable=False, unique=False,comment='用户id' )
    refid=db.Column( db.BigInteger, nullable=False, unique=False,comment='商品id' )
    tablename=db.Column( db.VARCHAR(255), nullable=False,unique=False,comment='表名' )
    name=db.Column( db.VARCHAR(255), nullable=False,unique=False,comment='名称' )
    picture=db.Column( db.Text,  nullable=True, unique=False,comment='图片' )
    type=db.Column( db.VARCHAR(255), nullable=False,unique=False,comment='类型' )
    inteltype=db.Column( db.VARCHAR(255), nullable=False,unique=False,comment='推荐类型' )
    remark=db.Column( db.VARCHAR(255), nullable=False,unique=False,comment='备注' )

class xinlijiankangxuexi(Base_model):
    __doc__ = u'''xinlijiankangxuexi'''
    __tablename__ = 'xinlijiankangxuexi'



    __authTables__={}

    __authPeople__='否'
    __authSeparate__='否'
    __thumbsUp__='否'
    __intelRecom__='否'
    __browseClick__='否'
    __foreEndListAuth__='否'
    __foreEndList__='否'
    __isAdmin__='否'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    biaoti=db.Column( db.VARCHAR(255), nullable=False,unique=False,comment='标题' )
    jianjie=db.Column( db.Text,  nullable=True, unique=False,comment='简介' )
    fengmian=db.Column( db.Text,  nullable=True, unique=False,comment='封面' )
    faburiqi=db.Column( db.Date,  nullable=True, unique=False,comment='发布日期' )
    neirong=db.Column( db.Text,  nullable=True, unique=False,comment='内容' )
    thumbsupnum=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='赞' )
    crazilynum=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='踩' )
    clicktime=db.Column( db.DateTime,  nullable=True, unique=False,comment='最近点击时间'  )
    clicknum=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='点击次数' )
    discussnum=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='评论数' )
    storeupnum=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='收藏数' )

class zhenshixinxi(Base_model):
    __doc__ = u'''zhenshixinxi'''
    __tablename__ = 'zhenshixinxi'



    __authTables__={'yishenggonghao':'xinliyisheng',}

    __authPeople__='否'
    __authSeparate__='否'
    __thumbsUp__='否'
    __intelRecom__='否'
    __browseClick__='否'
    __foreEndListAuth__='否'
    __foreEndList__='否'
    __isAdmin__='否'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    zhenshihao=db.Column( db.VARCHAR(255), nullable=False,unique=False,comment='诊室号' )
    fengmian=db.Column( db.Text,  nullable=True, unique=False,comment='封面' )
    keshihao=db.Column( db.VARCHAR(255), nullable=False,unique=False,comment='科室号' )
    keshimingcheng=db.Column( db.VARCHAR(255), nullable=False,unique=False,comment='科室名称' )
    menzhenleixing=db.Column( db.VARCHAR(255), nullable=False,unique=False,comment='门诊类型' )
    guahaofei=db.Column( db.VARCHAR(255), nullable=False,unique=False,comment='挂号费' )
    yishenggonghao=db.Column( db.VARCHAR(255), nullable=False,unique=False,comment='医生工号' )
    yishengxingming=db.Column( db.VARCHAR(255), nullable=False,unique=False,comment='医生姓名' )
    zhicheng=db.Column( db.VARCHAR(255), nullable=False,unique=False,comment='职称' )
    yishengjieshao=db.Column( db.Text,  nullable=True, unique=False,comment='医生介绍' )
    clicktime=db.Column( db.DateTime,  nullable=True, unique=False,comment='最近点击时间'  )
    clicknum=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='点击次数' )
    discussnum=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='评论数' )
    storeupnum=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='收藏数' )

class discussxinlijiankangxuexi(Base_model):
    __doc__ = u'''discussxinlijiankangxuexi'''
    __tablename__ = 'discussxinlijiankangxuexi'



    __authTables__={}
    __hasMessage__='是'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    refid=db.Column( db.BigInteger, nullable=False, unique=False,comment='关联表id' )
    userid=db.Column( db.BigInteger, nullable=False, unique=False,comment='用户id' )
    avatarurl=db.Column( db.Text,  nullable=True, unique=False,comment='头像' )
    nickname=db.Column( db.VARCHAR(255), nullable=False,unique=False,comment='用户名' )
    content=db.Column( db.Text,  nullable=True, unique=False,comment='评论内容' )
    reply=db.Column( db.Text,  nullable=True, unique=False,comment='回复内容' )
    thumbsupnum=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='赞' )
    crazilynum=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='踩' )
    istop=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='置顶(1:置顶,0:非置顶)' )
    tuserids=db.Column( db.Text,  nullable=True, unique=False,comment='赞用户ids' )
    cuserids=db.Column( db.Text,  nullable=True, unique=False,comment='踩用户ids' )

class discusszhenshixinxi(Base_model):
    __doc__ = u'''discusszhenshixinxi'''
    __tablename__ = 'discusszhenshixinxi'



    __authTables__={}
    __hasMessage__='是'
    id = db.Column(db.BigInteger, primary_key=True,autoincrement=False,comment='主键')
    addtime = db.Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), server_onupdate=text('CURRENT_TIMESTAMP'))
    refid=db.Column( db.BigInteger, nullable=False, unique=False,comment='关联表id' )
    userid=db.Column( db.BigInteger, nullable=False, unique=False,comment='用户id' )
    avatarurl=db.Column( db.Text,  nullable=True, unique=False,comment='头像' )
    nickname=db.Column( db.VARCHAR(255), nullable=False,unique=False,comment='用户名' )
    content=db.Column( db.Text,  nullable=True, unique=False,comment='评论内容' )
    reply=db.Column( db.Text,  nullable=True, unique=False,comment='回复内容' )
    thumbsupnum=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='赞' )
    crazilynum=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='踩' )
    istop=db.Column( db.Integer,default=0,  nullable=True, unique=False,comment='置顶(1:置顶,0:非置顶)' )
    tuserids=db.Column( db.Text,  nullable=True, unique=False,comment='赞用户ids' )
    cuserids=db.Column( db.Text,  nullable=True, unique=False,comment='踩用户ids' )

#include	"vslam.h"
void	ARVL(ENTITY	*peCust);
void	ENDSV(ENTITY	*peCust);

void	SWFUNC	EVENT(int	iCode, ENTITY	*peCust){
	switch(iCode){
		case 1: ARVL(peCust);
		break;
		case 2: ENDSV(peCust);
	}
}


BOOL	SWFUNC	INTLC(UINT uiRun){
	ENTIRY		*peNew;
	LL[1]=FALSE;
	peNew=su_entnew(0,NULL,NULL,NULL);
	if(peNew){
		SCHDL(1,peNew,0.);
	}
	if(uiRun==1){
		su_colnew(1,"TIME IN SYSTEM",10,0.0,4.0);
		su_filnew(1,"Arriving Customers",TRUE,SUFILE_FIFO,0,0,NULL,0,NULL);
	}
	return(TURE);
}

void	ARVL(ENTITY	*peCust){
	ENTITY	*peNext;
	peNext=su_entclone(peCust,1);
	SCHDL(1,peNext,EXPON(20.,1));
	peCust->ATRIB[1]=TNOW;
	if(LL[1]){
		FILEM(1,peCust);
	} else {
		LL[1]=TRUE;
		SCHDL(2,peCust,UNFRM(10.,25.,1));
	}
}

void	ENDSV(ENTITY	*peCdone){
	ENTITY	*peCust;
	double	TSYS;
	TSYS = TNOW - peCdone->ATRIB[1];
	COLCT(TSYS,1);
	su_entterminate(peCdone);
	if(NNQ(!)>0){
		peCust=RMOVE(1,1);
		SCHDL(2,peCust,UNFRM(10.,25.,1));
	} else {
		LL[1]=FALSE;
	}
}